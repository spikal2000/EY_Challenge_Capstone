import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import configparser

def insert_data_from_csv(table_name, csv_file_path, cursor):
    # Read data from CSV file
    df = pd.read_csv(csv_file_path)
    
    # Generate SQL query
    cols = ",".join([str(i) for i in df.columns.tolist()])
    
    # Iterate rows and format values
    for i, row in df.iterrows():
        sql = f"INSERT INTO {table_name} ({cols}) VALUES {tuple(row)}"
        
        # Execute the SQL statement
        cursor.execute(sql)

def main():
    config = configparser.ConfigParser()
    config.read('../configMysql.ini')

    db_config = {
        'user': config.get('mysql', 'user'),
        'password': config.get('mysql', 'password'),
        'host': config.get('mysql', 'host'),
        'port': config.get('mysql', 'port'),
        'database': 'rice_db'
    }

    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()

        # Assume that you have CSV files named 'RiceCrop.csv', 'Sentinel1.csv', 'NDVI.csv', 'WeatherParameters.csv'
        insert_data_from_csv('RiceCrop', 'RiceCrop.csv', cursor)
        insert_data_from_csv('Sentinel1', 'Sentinel1.csv', cursor)
        insert_data_from_csv('NDVI', 'NDVI.csv', cursor)
        insert_data_from_csv('WeatherParameters', 'WeatherParameters.csv', cursor)

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

if __name__ == "__main__":
    main()
