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

# session = Session(engine) # will need to comment this out when creating API

app = Flask(__name__)

@app.route("/")
def welcome():
    session = Session(engine)
    # crash_list = session.query(Crashes.CRASH_ID).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
    session.close()

    return (
        f"Welcome to our Oregon Crash App!"
        # jsonify(crash_dict)
    )

@app.route("/api/v1.0/crash_map")
def crash_map():
    session = Session(engine)

    results = session.query(Crashes.CRASH_DT).filter(Crashes.CRASH_EVNT_1_CD == 35).filter(dt.datetime.strptime(Crashes.CRASH_DT.tostring, "%m/%d/%Y") >= (dt.date(2019, 1, 1))).all()
    # results = session.query(Crashes.CRASH_DT).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
    # results = session.query(Crashes.CRASH_ID).all()
    
    session.close()

    print(len(results))
    
    deer_elk_crashes = np.ravel(results).tolist()

    print(len(deer_elk_crashes))

    return jsonify(deer_elk_crashes)
    #return("hello")

if __name__ == "__main__":
    app.run(debug=True)



# inspector = inspect(engine)
# print(inspector.get_table_names())
# columns = inspector.get_columns('oregon_crashes')
# for column in columns:
#     print(column["name"], column["type"])

# crash_list = session.query(Crashes.LAT_DD).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
# print(crash_list)
# date_list = session.query(Crashes.CRASH_DT).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
# print(date_list)
# crash_list_array = []
# for crash in crash_list:
#     crash_list_array.append(crash)

# print(len(crash_list_array))

# session.close() # will need to comment this out when creating API
