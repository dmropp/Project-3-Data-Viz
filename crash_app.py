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

#session = Session(engine) # will need to comment this out when creating API

@app.route("/")
def welcome():
    session = Session(engine)
    session.close()

    return (
        f"<h2 id='Welcome Page Header'>Welcome to our Oregon Crash App!</h2>" 
        f"<h3 id='Subheader'>Please use the following routes:</h3>"
        f"<p>/api/v1.0/crash_map for json data of all car crashes in Oregon involving wild animals<br>"
        f"/api/v1.0/dashboard for json data of all car crashes in Oregon involving wild animals<br>"
        f"/api/v1.0/map_viz for an interactive map illustrating the location of all call crashes in Oregon involving wild animals <br>"
        f"/api/v1.0/dashboard_viz for an interactive dashboard of statistics behind car crashes with wild animals in Oregon<p/>"
    )

@app.route("/api/v1.0/crash_map")
def crash_map():
    session = Session(engine)

    # Filter crash data by codes 34(wild game) and 35(deer or elk)
    results_1 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 34).all()

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

    # Create dictionary of filtered crash data
    animal_crashes = []
    results_list = [results_1, results_2, results_3, results_4, results_5, results_6]
    for result in results_list:
        for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in result:
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

    print(len(animal_crashes))

    return jsonify(animal_crashes)
    #return("hello")
    # data = jsonify(animal_crashes)
    # print(len(data))
    # return render_template("map_index.html", data=jsonify(animal_crashes))

@app.route("/api/v1.0/dashboard")
def dashboard():

    session = Session(engine)

    # Filter crash data by codes 34(wild game) and 35(deer or elk)
    results_1 = session.query(Crashes.CRASH_DT, Crashes.HWY_MED_NM, Crashes.LAT_DD, Crashes.LONGTD_DD, Crashes.CRASH_TYP_CD, Crashes.CRASH_TYP_SHORT_DESC, Crashes.CRASH_SVRTY_CD,
                            Crashes.CRASH_SVRTY_SHORT_DESC, Crashes.CRASH_EVNT_1_CD, Crashes.CRASH_EVNT_2_CD, Crashes.CRASH_EVNT_3_CD,
                            Crashes.CRASH_EVNT_1_SHORT_DESC, Crashes.CRASH_EVNT_2_SHORT_DESC, Crashes.CRASH_EVNT_3_SHORT_DESC,
                            Crashes.CRASH_CAUSE_1_CD, Crashes.CRASH_CAUSE_2_CD, Crashes.CRASH_CAUSE_3_CD, Crashes.CRASH_CAUSE_1_SHORT_DESC, 
                            Crashes.CRASH_CAUSE_2_SHORT_DESC, Crashes.CRASH_CAUSE_3_SHORT_DESC
                            ).\
        filter(Crashes.CRASH_EVNT_1_CD == 34).all()

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

    # Create dictionary of filtered crash data
    animal_crashes = []
    results_list = [results_1, results_2, results_3, results_4, results_5, results_6]
    for result in results_list:
        for date, hwy_name, lat, lng, crash_type, crash_type_desc, crash_severity, crash_severity_desc, crash_event_1, crash_event_2, crash_event_3, crash_event_1_desc, crash_event_2_desc, crash_event_3_desc, crash_cause_1, crash_cause_2, crash_cause_3, crash_cause_1_desc, crash_cause_2_desc, crash_cause_3_desc in result:
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
    
    print(len(animal_crashes))
          
    return jsonify(animal_crashes)
    # return render_template("dashboard_index.html", data=jsonify(animal_crashes))

# @app.route("/api/v1.0/map_viz") #see if I can create separate HTML file and use return(call HTML)
# def map_viz():
#     return(
#         f"<html lang='en'>"
#         f"<head>"
#             f"<meta charset='UTF-8'>"
#             f"<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
#             f"<meta http-equiv='X-UA Compatible' content='ie=edge'>"
#             f"<title>Oregon Crash Map</title>"
#             f"<link rel='stylesheet' href='https://unpkg.com/leaflet@1.9.4/dist/leaflet.css' integrity='sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=' crossorigin='' />" #leaflet stylesheet
#             # f"<link rel='stylesheet' type='text/css' href='FILEPATH'>" - link to our CSS style sheet
#         f"</head>" 
#         f"<body>"
#             f"<div id='map'></div>"
#             f"<script src='https://unpkg.com/leaflet@1.9.4/dist/leaflet.js' integrity='sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=' crossorigin=''></script>" #leaflet script
#             f"<script src='https://d3js.org/d3.v7.min.js'></script>" #D3 script
#             #f"<script src='http://127.0.0.1:5000/api/v1.0/crash_map'></script>"
#             #f"<script type='text/javascript' filename='.js/map_app_js.js'></script>" # link to our javascript
#             f"<script type='text/javascript' src='js/map_app_js.js'></script>"
#             #f"<script src='{{ url_for("static", filename='.js/map_app_js.js') }}></script>" # link to our javascript
#         f"</body>"
#     )

@app.route("/api/v1.0/map_viz") #see if I can create separate HTML file and use return(call HTML)
def map_viz():
    return render_template("map_index.html")
    
# Dashboard visualization page
# @app.route("/api/v1.0/dashboard_viz")
# def dashboard_viz():
#     return(
#         f"<html lang='en'>"
#         f"<head>"
#             f"<meta charset='UTF-8'>"
#             f"<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
#             f"<meta http-equiv='X-UA-Compatible' content='ie=edge'>"
#             f"<title>Oregon Crash Dashboard</title>"
#             f"<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>" # if we need custom CSS we can add the file to the head section
#         f"</head>"
#         f"<body>"
#             f"<div class='container'>"
#                 f"<div class='row'>"
#                     f"<div class='col-md-12 jumbotron text-center'>"
#                         f"<h1>Dashboard goes here</h1>"
#                         f"<h4>Use the interactive charts below to explore the dataset</h4>"
#                     f"</div>"
#                 f"</div>"
#                 f"<div class='row'>"
#                     f"<div class='col-md-2'>"
#                         f"<div class='well'>"
#                             f"<h5>Date:</h5>"
#                             f"<select id='selDate' onchange='optionChanged(this.value)'></select>" # Used the same code from the belly button challenge to handle the drop down menu
#                         f"</div>"
#                     f"</div>"
#                     f"<div class='col-md-5'>"
#                         f"<div id='bar'></div>"
#                     f"</div>"
#                     f"<div class='col-md-5'>"
#                         f"<div id='plot'></div>"
#                     f"</div>"
#                 f"</div>"
#             f"</div>"
#             f"<script src='https://d3js.org/d3.v7.min.js'></script>" #D3 script 
#             f"<script src='https://cdn.plot.ly/plotly-latest.min.js'></script>" #Plotly script
#             #f"<script src='FILEPATH'></script>" our javascript file
#         f"</body>"   
#         f"</html>"         
#     )

@app.route("/api/v1.0/dashboard_viz")
def dashboard_viz():
    return render_template("dashboard_index.html")

if __name__ == "__main__":
    app.run(debug=True)


# debugging
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
