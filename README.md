# Project-3-Data-Viz

## Vehicle Accidents in Oregon Involving Deer and Elk

The purpose of this project is to identify hotspots for vehicle collisions involving deer and elk in order to better determine where safety improvements via signage or road modification needs to be prioritized to improve safety for drivers and animals. This will be achieved via mapping and an interactive dashboard. 

-  The map will have markers for each crash incident by year. - PopUps - include crash code and severity
-  Bar chart of the top 10 routes for deer or elk-involved collisions.
-  A line chart of deer or elk-involved collisions over time.

Data Source - https://www.oregon.gov/odot/Data/Pages/CrashDataProducts.aspx?wp8625=f%3a%7bc%3a38877%2co%3a%7bt%3a2%2co%3a%5b%22Decode+Database%22%5d%7d%7d

Data Used

- Crash ID - CRASH_ID
- Date - CRASH_DT
- Longitude - LONGTD_DD
- Latitude - LAT_DD
- Crash Type - CRASH_EVNT_1_CD (codes 034, 035)
- Crash Type Description - CRASH_EVNT_1_SHORT_DESC
- Route Name - HWY_MED_NM
- Crash Severity - CRASH.SVRTY_CD

https://www.sqlite.org/cli.html, referenced for how to create SQLite database in command line.
