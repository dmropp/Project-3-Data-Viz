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

# Crashes = Base.classes.oregon_crashes

print(Base.classes.keys())

app = Flask(__name__)

# @app.route("/")
# def welcome():
#     session = Session(engine)
#     # crash_list = session.query(Crashes.CRASH_ID).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
#     session.close()

#     return (
#         f"Welcome to our Oregon Crash App!"
#         # jsonify(crash_dict)
#     )

# if __name__ == "__main__":
#     app.run(debug=True)



inspector = inspect(engine)
print(inspector.get_table_names())
# columns = inspector.get_columns('oregon_crashes')
# for column in columns:
#     print(column["name"], column["type"])

# data = engine.execute("SELECT CRASH_ID FROM oregon_crashes WHERE CRASH_EVNT_1_CD = 035;")
# data = engine.execute("SELECT CRASH_EVNT_SHORT_DESC FROM oregon_crashes")
# deer_crashes = []
# for record in data:
#     deer_crashes.append(record)
# print(len(deer_crashes))

# crash_list = session.query(Crashes.CRASH_ID).filter(Crashes.CRASH_EVNT_1_CD == 35).all()
# print(len(crash_list))
# crash_list_array = []
# for crash in crash_list:
#     crash_list_array.append(crash)

# print(len(crash_list_array))

# session.close()
