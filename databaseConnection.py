import mysql.connector
import configparser


class databaseConnection:

    def databaseConnect(self):

        try:
            config = configparser.ConfigParser()
            config.read('database.properties')

            host = config['MYSQL']['host']
            port = config['MYSQL']['port']
            database = config['MYSQL']['database']
            user = config['MYSQL']['user']
            password = config['MYSQL']['password']
            connection = mysql.connector.connect(host=host,port=port, database=database, user=user, password = password)

            #also return other configurations
            ALGORITHM = config['CONFIGS']['ALGORITHM']
            SECRET_KEY = config['CONFIGS']['SECRET_KEY']

            return connection
        except Exception as e:
            print("error connection database ",e)





