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
RAPI_Table_Stations = StationsFromRestApi.loc[:,["id","stationName","gegrLat","gegrLon","addressStreet","city.id","city.id","city.name","city.commune.communeName","city.commune.districtName","city.commune.provinceName"]].set_index('id')
DB_Table_Stations = TableFromDB('dbo.AllStations',ConString).set_index('id')
RAPI_Table_StationsCities = pd.merge(RAPI_Table_Stations,DB_Table_Stations, how='left',on=['id'],suffixes=('_left','_right')).query('stationName_right.isnull()')
print(RAPI_Table_StationsCities.head())
#print(RAPI_Table_StationsCities)
#DimenstionStations = pd.merRAPI_Table_Stations
#DimensionStations = StationsFromRestApi.loc[:,["id","stationName","city","addressStreet"]]
# StationsIds = StationsFromRestApi.loc[:,["id"]]
# All = (GiveMeAllAvaiableSensor(StationsIds))
# SensorData = (GiveMeDataFromStationsSensors(All))
# StationsFromDB = TableFromDB('dbo.AllStations',ConString)