import requests
import pyodbc as db
import pandas as pd
from sqlalchemy import create_engine
import urllib

def GetDataFromApi(URL):
    response = requests.get(URL)
    if (response.status_code == 200):        
        return response.json()
    elif (response.status_code == 404):
        print("Result not found!")

def truncateTable(TableName, Connection):
    Query = 'truncate table '+TableName
    Connection.execute(Query)
    Connection.commit()

def TableFromDB(TableName, Connection):
    Query = "SELECT * FROM "+TableName
    df = pd.read_sql(Query,Connection)
    return df

def ConnStringBuild(Server, Database):
    params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER="+Server+";"
                                 "DATABASE="+Database+";"
                                 "Trusted_Connection=yes")
    conn = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    return conn

def FromRawDataToStgTable(Type, Source):
    if Type == "RestApi":
        RawDataFrame = pd.DataFrame(Source)
    else:
        print('That type is incompatible with FromRawDataToStgTable function')

def GiveMeAllAvaiableSensor (Stations):
    for StId in Stations.itertuples():
        AvaiableSensors = 'https://api.gios.gov.pl/pjp-api/rest/station/sensors/'+str(StId.id)
        return pd.DataFrame(GetDataFromApi(AvaiableSensors))


def GiveMeDataFromStationsSensors(SensorCollections):
    for sensorid in SensorCollections.itertuples():
        DataFromSensor = 'https://api.gios.gov.pl/pjp-api/rest/data/getData/'+str(sensorid.id)        
        return pd.DataFrame(GetDataFromApi(DataFromSensor))
