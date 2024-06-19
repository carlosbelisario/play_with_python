import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def connect():
    db_host = os.getenv('DATABASE_HOST')
    db_name = os.getenv('DATABASE_NAME')
    db_user = os.getenv('DATABASE_USER')
    db_password = os.getenv('DATABASE_PASSWORD')
    db_port = os.getenv('DATABASE_PORT')
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            database=db_name
        )
        if connection.is_connected():
            # print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")