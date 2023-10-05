import warnings
warnings.filterwarnings("ignore")

import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify, render_template

engine = create_engine("sqlite:///oregon_crashes.sqlite")

Base = automap_base()

Base.prepare(autoload_with=engine)

Crashes = Base.classes.oregon_crashes

print(Base.classes.keys())

app = Flask(__name__)

@app.route("/")
def welcome():
    session = Session(engine)
    session.close()

    return ( # https://www.w3schools.com/html/html_links.asp, referenced for how to use HTML links
        f"<h2 id='Welcome Page Header'>Welcome to our Oregon Crash App!</h2>" 
        f"<h3 id='Subheader'>Please use the following routes:</h3>"
        f"<p>/"
        f"<a href='http://127.0.0.1:5000/map_data'>map_data </a>"
        f"for json data of all car crashes in Oregon involving wild animals<br>"
        f"/<a href='http://127.0.0.1:5000/dashboard_data'>dashboard_data </a>"
        f"for json data of all car crashes in Oregon involving wild animals<br>"
        f"/<a href='http://127.0.0.1:5000/map'>map </a>"
        f"for an interactive map illustrating the location of all call crashes in Oregon involving wild animals <br>"
        f"/<a href='http://127.0.0.1:5000/dashboard'>dashboard </a>"
        f"for an interactive dashboard of statistics behind car crashes with wild animals in Oregon<p/>"
    )

@app.route("/map_data")
def crash_map():
    session = Session(engine)

    # Filter crash data by codes 34(wild game) and 35(deer or elk)
    results_1 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 34).all()

    results_2 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 35).all()
    
    results_3 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_2_CD == 34).all()
    
    results_4 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                        Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                        Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                        Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                        Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                        ).\
        filter(Crashes.CRASH_EVNT_2_CD == 35).all()

    results_5 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                    Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                    Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                    Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                    Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                    ).\
        filter(Crashes.CRASH_EVNT_3_CD == 34).all()
    
    results_6 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                    Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                    Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                    Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                    Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                    ).\
        filter(Crashes.CRASH_EVNT_3_CD == 35).all()
        
    session.close()

    # Create dictionary of filtered crash data
    animal_crashes = []
    results_list = [results_1, results_2, results_3, results_4, results_5, results_6]
    for result in results_list:
        for date, year, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in result:
            crash_dict = {}
            crash_dict["date"] = date
            crash_dict["year"] = year
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

    print(len(animal_crashes))

    return jsonify(animal_crashes)

@app.route("/dashboard_data")
def dashboard():

    session = Session(engine)

    # Filter crash data by codes 34(wild game) and 35(deer or elk)
    results_1 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 34).all()

    results_2 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 35).all()
    
    results_3 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_2_CD == 34).all()
    
    results_4 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                        Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                        Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                        Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                        Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                        ).\
        filter(Crashes.CRASH_EVNT_2_CD == 35).all()

    results_5 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                    Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                    Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                    Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                    Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                    ).\
        filter(Crashes.CRASH_EVNT_3_CD == 34).all()
    
    results_6 = session.query(Crashes.CRASH_DT, Crashes.CRASH_YR_NO, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                    Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                    Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                    Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                    Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                    ).\
        filter(Crashes.CRASH_EVNT_3_CD == 35).all()
    
    session.close()

    # Create dictionary of filtered crash data
    animal_crashes = []
    results_list = [results_1, results_2, results_3, results_4, results_5, results_6]
    for result in results_list:
        for date, year, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in result:
            crash_dict = {}
            crash_dict["date"] = date
            crash_dict["year"] = year
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
    
    print(len(animal_crashes))
          
    return jsonify(animal_crashes)

@app.route("/map")
def map_viz():
    return render_template("map_index.html")

@app.route("/dashboard")
def dashboard_viz():
    return render_template("dashboard_index.html")

if __name__ == "__main__":
    app.run(debug=True)
