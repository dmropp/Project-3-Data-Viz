import sqlite3
import pandas as pd

from pathlib import Path

database_path = "oregon_crashes.sqlite"

Path(database_path).touch()

conn = sqlite3.connect(database_path)
c = conn.cursor()

c.execute('''CREATE TABLE crashes (ID int)''')

# csv_crashes_2016 = pd.read_csv("/Data/CRASH_2016.csv")
# csv_

conn.close()