import pandas as pd
import json
import pyodbc as db
from RestApiTools.Functions import *
import matplotlib.pyplot as plt


AllStatURL = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
ConString = ConnStringBuild('.','Sandbox')
StationsJSON = (GetDataFromApi(AllStatURL))

FromRawDataToStgTable('RestApi',StationsJSON)
StationsFromRestApi = pd.json_normalize(StationsJSON,max_level=2)
print(StationsFromRestApi)
print(StationsFromRestApi.loc[:,["id","stationName","city.id","city.name"]])
#DimensionStations = StationsFromRestApi.loc[:,["id","stationName","city","addressStreet"]]
# StationsIds = StationsFromRestApi.loc[:,["id"]]
# All = (GiveMeAllAvaiableSensor(StationsIds))
# SensorData = (GiveMeDataFromStationsSensors(All))
# StationsFromDB = TableFromDB('dbo.AllStations',ConString)