import warnings
warnings.filterwarnings("ignore")

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

engine = create_engine("sqlite:///oregon_crashes.sqlite")

Base = automap_base()

Base.prepare(autoload_with=engine)

Crashes = Base.classes.oregon_crashes

print(Base.classes.keys())

app = Flask(__name__)

#session = Session(engine) # will need to comment this out when creating API

@app.route("/")
def welcome():
    session = Session(engine)
    # Add HTML for welcome screen
    session.close()

    return (
        f"Welcome to our Oregon Crash App!"
        # jsonify(crash_dict)
    )

@app.route("/api/v1.0/crash_map")
def crash_map():
    session = Session(engine)

    results = session.query(Crashes.CRASH_DT, Crashes.LAT_DD, Crashes.HWY_MED_NM, Crashes.LONGTD_DD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 35).all() # store lat, long, roadway desc, crash type, crash severity in dict for map
    
    session.close()

    print(len(results))
    
    # deer_elk_crashes = np.ravel(results).tolist()
    animal_crash_dict = dict(results)

    print(len(animal_crash_dict))

    return jsonify(animal_crash_dict)
    #return("hello")

if __name__ == "__main__":
    app.run(debug=True)



# inspector = inspect(engine)
# print(inspector.get_table_names())
# columns = inspector.get_columns('oregon_crashes')
# for column in columns:
#     print(column["name"], column["type"])

# crash_list = session.query(Crashes.LAT_DD).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
# print(len(crash_list))
# date_list = session.query(Crashes.CRASH_DT).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
# print(date_list)
# crash_list_array = []
# for crash in crash_list:
#     crash_list_array.append(crash)

# print(len(crash_list_array))

# session.close() # will need to comment this out when creating API
