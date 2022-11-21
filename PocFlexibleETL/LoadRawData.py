import pandas as pd
import pyodbc as db
from RestApiTools.Functions import *
import matplotlib.pyplot as plt


AllStatURL = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
ConString = ConnStringBuild('.','Sandbox')
StationsJSON = (GetDataFromApi(AllStatURL))

FromRawDataToStgTable('RestApi',StationsJSON)
df = pd.DataFrame(StationsJSON)
Stations = df.loc[:,["id"]]
All = (GiveMeAllAvaiableSensor(Stations))
SensorData = (GiveMeDataFromStationsSensors(All))
print(All)