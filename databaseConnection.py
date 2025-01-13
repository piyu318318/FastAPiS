import mysql.connector
import configparser


class databaseConnection:

    def databaseConnect(self):

        try:
            config = configparser.ConfigParser()
            config.read('database.properties')

            host = config['DEFAULT']['host']
            port = config['DEFAULT']['port']
            database = config['DEFAULT']['database']
            user = config['DEFAULT']['user']
            password = config['DEFAULT']['password']
            connection = mysql.connector.connect(host=host,port=port, database=database, user=user, password = password)

            return connection
        except Exception as e:
            print("error connection database ",e)





