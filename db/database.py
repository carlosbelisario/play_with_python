import mysql.connector

def connect():
    db_host = 'localhost'
    db_name = 'cars'
    db_user = 'root'
    db_password = 'asdf'
    db_port = '3340' # por default es 3306
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