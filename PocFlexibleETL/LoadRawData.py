import pandas as pd
import pyodbc as db
from RestApiTools.Functions import *

AllStatURL = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
conn = db.connect('Driver={SQL Server};'
                       'Server=.;'
                       'Database=Sandbox;'
                       'Trusted_Connection=yes;')
StationsJSON = (GetDataFromApi(AllStatURL))
df = pd.DataFrame(StationsJSON)
TableStations = df.loc[:,["stationName","id","gegrLat","gegrLon","city","addressStreet"]]
truncateTable('[dbo].[AllStations]',conn)