from fastapi import FastAPI
from databaseConnection import databaseConnection
app = FastAPI()


databaseClassObj = databaseConnection()
connection = databaseClassObj.databaseConnect()
cursor = connection.cursor()