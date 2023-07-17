import mysql.connector
import pandas as pd
from mysql.connector import errorcode
import configparser

config = configparser.ConfigParser()
config.read('../configMysql.ini')

db_config = {
    'user': config.get('mysql', 'user'),
    'password': config.get('mysql', 'password'),
    'host': config.get('mysql', 'host'),
    'port': config.get('mysql', 'port'),
    'database': 'rice_db'
}

from datetime import datetime

def insert_data_from_csv(table_name, csv_file_path, cursor, column_mapping):
    # Read data from CSV file
    df = pd.read_csv(csv_file_path)
    
    # Map CSV column names to database column names
    df = df.rename(columns=column_mapping)
    
    # Convert date format
    df['DateOfHarvest'] = df['DateOfHarvest'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y').strftime('%Y-%m-%d'))
    
    # Generate SQL query
    cols = ",".join([f"`{str(i)}`" for i in df.columns.tolist()])
    
    # Iterate rows and format values
    for i, row in df.iterrows():
        values = tuple(row.values)
        sql = f"INSERT INTO {table_name} ({cols}) VALUES {values}"
        
        # Execute the SQL statement
        try:
            cursor.execute(sql)
        except mysql.connector.Error as err:
            print(f"Error occurred: {err}")
            print(f"Failed SQL: {sql}")


try:
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    cursor.execute("USE rice_db")

    # Column mapping for RiceCrop table
    ricecrop_column_mapping = {
    'District': 'district',
    'Latitude': 'latitude',
    'Longitude': 'longitude',
    'Season(SA = Summer Autumn, WS = Winter Spring)': 'Season',
    'Rice Crop Intensity(D=Double, T=Triple)': 'RiceCropIntensity',
    'Date of Harvest': 'DateOfHarvest',
    'Field size (ha)': 'FieldSize',
    'Rice Yield (kg/ha)': 'RiceYield'
    }


    # Insert data from RiceCrop.csv
    insert_data_from_csv('RiceCrop', r'C:\Users\spika\Desktop\git\EY_Challenge_Capstone\Data\Crop_Yield_Data_challenge_2.csv', cursor, ricecrop_column_mapping)

    # Column mapping for Sentinel1 table
    # sentinel1_column_mapping = {
    #     'CSV_Column1': 'db_column1',
    #     'CSV_Column2': 'db_column2',
    #     # ...
    # }

    # Insert data from Sentinel1.csv
    # insert_data_from_csv('Sentinel1', 'Sentinel1.csv', cursor, sentinel1_column_mapping)

    # Column mapping for NDVI table
    # ndvi_column_mapping = {
    #     'CSV_Column1': 'db_column1',
    #     'CSV_Column2': 'db_column2',
    #     # ...
    # }

    # Insert data from NDVI.csv
    # insert_data_from_csv('NDVI', 'NDVI.csv', cursor, ndvi_column_mapping)

    # Column mapping for WeatherParameters table
    # weather_column_mapping = {
    #     'CSV_Column1': 'db_column1',
    #     'CSV_Column2': 'db_column2',
    #     # ...
    # }

    # Insert data from WeatherParameters.csv
    # insert_data_from_csv('WeatherParameters', 'WeatherParameters.csv', cursor, weather_column_mapping)

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
