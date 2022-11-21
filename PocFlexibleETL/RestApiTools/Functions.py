import requests
import pyodbc as db
import pandas as pd
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

def ConnStringBuild(Server, Database):
    conn = db.connect('Driver={SQL Server};'
                       'Server=' + Server + ';'
                       'Database='+ Database + ';'
                       'Trusted_Connection=yes;')
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
        print(DataFromSensor)
        return pd.DataFrame(GetDataFromApi(DataFromSensor))
