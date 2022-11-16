import requests
import pyodbc as db
def GetDataFromApi(URL):
    response = requests.get(URL)
    if (response.status_code == 200):
        print("The request was a success!")
        return response.json()
    elif (response.status_code == 404):
        print("Result not found!")

def truncateTable(TableName, Connection):
    Query = 'truncate table '+TableName
    Connection.execute(Query)
    Connection.commit()