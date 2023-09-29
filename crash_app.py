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

    results_1 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 34).all()
        
        
        # filter(Crashes.CRASH_EVNT_1_CD == 34 | Crashes.CRASH_EVNT_1_CD == 35 | Crashes.CRASH_EVNT_2_CD == 34 | Crashes.CRASH_EVNT_2_CD == 35 | Crashes.CRASH_EVNT_3_CD == 34 | Crashes.CRASH_EVNT_3_CD == 35).all()
    
        # filter(Crashes.CRASH_EVNT_1_CD == 34).filter(Crashes.CRASH_EVNT_1_CD == 35).filter(Crashes.CRASH_EVNT_2_CD == 34).filter(Crashes.CRASH_EVNT_2_CD == 35).\
        # filter(Crashes.CRASH_EVNT_3_CD == 34).filter(Crashes.CRASH_EVNT_3_CD == 35).all() # store lat, long, roadway desc, crash type, crash severity in dict for map

    results_2 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 35).all()
    
    results_3 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_2_CD == 34).all()
    
    results_4 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                        Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                        Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                        Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                        Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                        ).\
        filter(Crashes.CRASH_EVNT_2_CD == 35).all()

    results_5 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                    Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                    Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                    Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                    Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                    ).\
        filter(Crashes.CRASH_EVNT_3_CD == 34).all()
    
    results_6 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                    Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                    Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                    Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                    Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                    ).\
        filter(Crashes.CRASH_EVNT_3_CD == 35).all()
        
    session.close()

    #print(results)

    animal_crashes = []
    for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in results_1:
        crash_dict = {}
        crash_dict["date"] = date
        crash_dict["hwy_name"] = hwy_name
        crash_dict["lat"] = lat
        crash_dict["lng"] = lng
        crash_dict["crash_type"] = crash_type
        crash_dict["crash_type_desc"] = crash_type_desc
        crash_dict["crash_severity"] = crash_severity
        crash_dict["crash_severity_desc"] = crash_severity_desc
        crash_dict["crash_event_1"] = crash_event_1
        crash_dict["crash_event_2"] = crash_event_2
        crash_dict["crash_event_3"] = crash_event_3
        crash_dict["crash_event_1_desc"] = crash_event_1_desc
        crash_dict["crash_event_2_desc"] = crash_event_2_desc
        crash_dict["crash_event_3_desc"] = crash_event_3_desc
        crash_dict["crash_cause_1"] = crash_cause_1
        crash_dict["crash_cause_2"] = crash_cause_2
        crash_dict["crash_cause_3"] = crash_cause_3
        crash_dict["crash_cause_1_desc"] = crash_cause_1_desc
        crash_dict["crash_cause_2_desc"] = crash_cause_2_desc
        crash_dict["crash_cause_3_desc"] = crash_cause_3_desc
        animal_crashes.append(crash_dict)
    
    #animal_crashes_2 = []
    for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in results_2:
        crash_dict = {}
        crash_dict["date"] = date
        crash_dict["hwy_name"] = hwy_name
        crash_dict["lat"] = lat
        crash_dict["lng"] = lng
        crash_dict["crash_type"] = crash_type
        crash_dict["crash_type_desc"] = crash_type_desc
        crash_dict["crash_severity"] = crash_severity
        crash_dict["crash_severity_desc"] = crash_severity_desc
        crash_dict["crash_event_1"] = crash_event_1
        crash_dict["crash_event_2"] = crash_event_2
        crash_dict["crash_event_3"] = crash_event_3
        crash_dict["crash_event_1_desc"] = crash_event_1_desc
        crash_dict["crash_event_2_desc"] = crash_event_2_desc
        crash_dict["crash_event_3_desc"] = crash_event_3_desc
        crash_dict["crash_cause_1"] = crash_cause_1
        crash_dict["crash_cause_2"] = crash_cause_2
        crash_dict["crash_cause_3"] = crash_cause_3
        crash_dict["crash_cause_1_desc"] = crash_cause_1_desc
        crash_dict["crash_cause_2_desc"] = crash_cause_2_desc
        crash_dict["crash_cause_3_desc"] = crash_cause_3_desc
        animal_crashes.append(crash_dict)
    
    #animal_crashes_3 = []
    for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in results_3:
        crash_dict = {}
        crash_dict["date"] = date
        crash_dict["hwy_name"] = hwy_name
        crash_dict["lat"] = lat
        crash_dict["lng"] = lng
        crash_dict["crash_type"] = crash_type
        crash_dict["crash_type_desc"] = crash_type_desc
        crash_dict["crash_severity"] = crash_severity
        crash_dict["crash_severity_desc"] = crash_severity_desc
        crash_dict["crash_event_1"] = crash_event_1
        crash_dict["crash_event_2"] = crash_event_2
        crash_dict["crash_event_3"] = crash_event_3
        crash_dict["crash_event_1_desc"] = crash_event_1_desc
        crash_dict["crash_event_2_desc"] = crash_event_2_desc
        crash_dict["crash_event_3_desc"] = crash_event_3_desc
        crash_dict["crash_cause_1"] = crash_cause_1
        crash_dict["crash_cause_2"] = crash_cause_2
        crash_dict["crash_cause_3"] = crash_cause_3
        crash_dict["crash_cause_1_desc"] = crash_cause_1_desc
        crash_dict["crash_cause_2_desc"] = crash_cause_2_desc
        crash_dict["crash_cause_3_desc"] = crash_cause_3_desc
        animal_crashes.append(crash_dict)
    
    #animal_crashes_4 = []
    for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in results_4:
        crash_dict = {}
        crash_dict["date"] = date
        crash_dict["hwy_name"] = hwy_name
        crash_dict["lat"] = lat
        crash_dict["lng"] = lng
        crash_dict["crash_type"] = crash_type
        crash_dict["crash_type_desc"] = crash_type_desc
        crash_dict["crash_severity"] = crash_severity
        crash_dict["crash_severity_desc"] = crash_severity_desc
        crash_dict["crash_event_1"] = crash_event_1
        crash_dict["crash_event_2"] = crash_event_2
        crash_dict["crash_event_3"] = crash_event_3
        crash_dict["crash_event_1_desc"] = crash_event_1_desc
        crash_dict["crash_event_2_desc"] = crash_event_2_desc
        crash_dict["crash_event_3_desc"] = crash_event_3_desc
        crash_dict["crash_cause_1"] = crash_cause_1
        crash_dict["crash_cause_2"] = crash_cause_2
        crash_dict["crash_cause_3"] = crash_cause_3
        crash_dict["crash_cause_1_desc"] = crash_cause_1_desc
        crash_dict["crash_cause_2_desc"] = crash_cause_2_desc
        crash_dict["crash_cause_3_desc"] = crash_cause_3_desc
        animal_crashes.append(crash_dict)

    #animal_crashes_5 = []
    for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in results_5:
        crash_dict = {}
        crash_dict["date"] = date
        crash_dict["hwy_name"] = hwy_name
        crash_dict["lat"] = lat
        crash_dict["lng"] = lng
        crash_dict["crash_type"] = crash_type
        crash_dict["crash_type_desc"] = crash_type_desc
        crash_dict["crash_severity"] = crash_severity
        crash_dict["crash_severity_desc"] = crash_severity_desc
        crash_dict["crash_event_1"] = crash_event_1
        crash_dict["crash_event_2"] = crash_event_2
        crash_dict["crash_event_3"] = crash_event_3
        crash_dict["crash_event_1_desc"] = crash_event_1_desc
        crash_dict["crash_event_2_desc"] = crash_event_2_desc
        crash_dict["crash_event_3_desc"] = crash_event_3_desc
        crash_dict["crash_cause_1"] = crash_cause_1
        crash_dict["crash_cause_2"] = crash_cause_2
        crash_dict["crash_cause_3"] = crash_cause_3
        crash_dict["crash_cause_1_desc"] = crash_cause_1_desc
        crash_dict["crash_cause_2_desc"] = crash_cause_2_desc
        crash_dict["crash_cause_3_desc"] = crash_cause_3_desc
        animal_crashes.append(crash_dict)
    
    #animal_crashes_6 = []
    for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in results_6:
        crash_dict = {}
        crash_dict["date"] = date
        crash_dict["hwy_name"] = hwy_name
        crash_dict["lat"] = lat
        crash_dict["lng"] = lng
        crash_dict["crash_type"] = crash_type
        crash_dict["crash_type_desc"] = crash_type_desc
        crash_dict["crash_severity"] = crash_severity
        crash_dict["crash_severity_desc"] = crash_severity_desc
        crash_dict["crash_event_1"] = crash_event_1
        crash_dict["crash_event_2"] = crash_event_2
        crash_dict["crash_event_3"] = crash_event_3
        crash_dict["crash_event_1_desc"] = crash_event_1_desc
        crash_dict["crash_event_2_desc"] = crash_event_2_desc
        crash_dict["crash_event_3_desc"] = crash_event_3_desc
        crash_dict["crash_cause_1"] = crash_cause_1
        crash_dict["crash_cause_2"] = crash_cause_2
        crash_dict["crash_cause_3"] = crash_cause_3
        crash_dict["crash_cause_1_desc"] = crash_cause_1_desc
        crash_dict["crash_cause_2_desc"] = crash_cause_2_desc
        crash_dict["crash_cause_3_desc"] = crash_cause_3_desc
        animal_crashes.append(crash_dict)
    # deer_elk_crashes = np.ravel(results).tolist()
    #animal_crash_dict = dict(results)

    print(len(animal_crashes))

    return jsonify(animal_crashes)
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
