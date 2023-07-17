import mysql.connector
from mysql.connector import errorcode
import configparser

config = configparser.ConfigParser()
config.read('../configMysql.ini')

db_config = {
    'user': config.get('mysql', 'user'),
    'password': config.get('mysql', 'password'),
    'host': config.get('mysql', 'host'),
    'port': config.get('mysql', 'port')
}

try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS rice_db")
    cursor.execute("USE rice_db")   

    query1 = """
    CREATE TABLE RiceCrop (
        id INT AUTO_INCREMENT PRIMARY KEY,
        district VARCHAR(80),
        latitude FLOAT,
        longitude FLOAT,
        Season VARCHAR(80),
        RiceCropIntensity VARCHAR(80),
        DateOfHarvest DATE,
        FieldSize FLOAT,
        RiceYield FLOAT
    )
    """

    query2 = """
    CREATE TABLE Sentinel1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        min_vh FLOAT,
        min_vv FLOAT,
        max_vh FLOAT,
        max_vv FLOAT,
        range_vh FLOAT,
        range_vv FLOAT,
        mean_vh FLOAT,
        mean_vv FLOAT,
        std_vh FLOAT,
        std_vv FLOAT,
        ratio_vv_vh FLOAT,
        rvi FLOAT,
        main_id INT,
        FOREIGN KEY(main_id) REFERENCES RiceCrop(id)
    )
    """

    query3 = """
    CREATE TABLE NDVI (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ndvi_value FLOAT,
        main_id INT,
        FOREIGN KEY(main_id) REFERENCES RiceCrop(id)
    )
    """

    query4 = """
    CREATE TABLE WeatherParameters (
        id INT AUTO_INCREMENT PRIMARY KEY,
        latitude FLOAT,
        longitude FLOAT,
        season VARCHAR(80),
    """

    parameters = ['tempmax', 'tempmin', 'temp', 'dew', 'humidity', 'precip', 
                  'precipcover', 'windgust', 'windspeed', 'pressure', 'cloudcover', 
                  'solarradiation', 'solarenergy', 'uvindex', 'SunlightDuration']
    
    for param in parameters:
        for i in range(1, 15):
            query4 += f"{param}_section_{i} FLOAT,"
    
    query4 += "main_id INT, FOREIGN KEY(main_id) REFERENCES RiceCrop(id)"
    
    query4 += ")"
    
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)

    cnx.commit()
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    if cnx:
        cnx.close()
