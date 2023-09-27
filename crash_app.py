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

print(Base.classes.keys())

session = Session(engine)

inspector = inspect(engine)
print(inspector.get_table_names())
columns = inspector.get_columns

session.close()
