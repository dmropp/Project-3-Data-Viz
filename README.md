# Project-3-Data-Viz

## Vehicle Accidents in Oregon Involving Deer and Elk

The purpose of this project is to identify hotspots for vehicle collisions involving deer and elk in order to better determine where safety improvements via signage or road modification needs to be prioritized to improve safety for drivers and animals. This will be achieved via mapping and an interactive dashboard. 

-  The map will have markers for each crash incident. PopUps - include crash code and severity
-  Bar chart of the top 10 routes for wild game, deer or elk-involved collisions.
-  A bar chart of wild game, deer, or elk-involved collisions over time.
-  A pie chart of crash severity with wild game, deer, or wild game.

## How to Use the Application
* create_sqlite_db.py - File to create the SQLite database from the original CSV files (CRASH_2016.csv, CRASH_2017.csv, CRASH_2018.csv, CRASH_2019.csv, CRASH_2020.csv, CRASH_2021.csv).
* crash_app.py - Oregon crash visualization app. Run this app to utilize the web interface.

## Data Source 
- https://www.oregon.gov/odot/Data/Pages/CrashDataProducts.aspx?wp8625=f%3a%7bc%3a38877%2co%3a%7bt%3a2%2co%3a%5b%22Decode+Database%22%5d%7d%7d

### Data Used

- Crash ID - CRASH_ID
- Date - CRASH_DT
- Year - CRASH_YR_NO
- Route Name - HWY_MED_NM
- Latitude - LAT_DD
- Longitude - LONGTD_DD
- Crash Type - CRASH_TYP_CD
- Crash Type Description - CRASH_TYP_SHORT_DESC
- Crash Severity - CRASH_SVRTY_CD
- Crash Severity Description - CRASH_SVRTY_SHORT_DESC
- Crash Type - CRASH_EVNT_1_CD, CRASH_EVNT_2_CD, CRASH_EVNT_3_CD (codes 034 - GAME, 035 - DEER ELK)
- Crash Type Description - CRASH_EVNT_1_SHORT_DESC, CRASH_EVNT_2_SHORT_DESC, CRASH_EVNT_3_SHORT_DESC
- Crash Cause - CRASH_CAUSE_1_CD, CRASH_CAUSE_2_CD, CRASH_CAUSE_3_CD
- Crash Cause Description - CRASH_CAUSE_1_SHORT_DESC, CRASH_CAUSE_2_SHORT_DESC, CRASH_CAUSE_3_SHORT_DESC

## References
- https://www.sqlite.org/cli.html, referenced for how to create SQLite database in command line.
- https://realpython.com/flask-javascript-frontend-for-rest-api/#step-2-build-the-front-end-components, referenced for overall project scope and how to call javascript files in HTML
- https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451, referenced for overall project scope
All other references are commented in the relevent line of code.
