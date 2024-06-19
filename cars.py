from db.database import connect

def create_car(brand, model, color):
    #conexion con base de datos
    db = connect()
    c = db.cursor()
    #creamos sentencia para insertar datos
    query = """INSERT INTO `cars` (brand_id, model, color) VALUES(%s, %s, %s)"""
    data = [(brand, model, color)]
    #ejecutamos el query
    c.executemany(query, data)
    #hacemos commit en la db
    db.commit()
    db.close()

def get_car(id):
    #conexion con base de datos
    db = connect()
    c = db.cursor()
    #creamos sentencia para insertar datos
    query = """SELECT * FROM `cars` where id = %s"""
    data = [(id)]
    #ejecutamos el query
    c.execute(query, data)
    car = c.fetchone()
    db.close()
    return car

def get_all_car():
    #conexion con base de datos
    db = connect()
    c = db.cursor()
    #creamos sentencia para insertar datos
    query = """SELECT * FROM `cars`"""
    #ejecutamos el query
    c.execute(query)
    cars = c.fetchall()
    db.close()
    return cars

def delete_car(id):
    #conexion con base de datos
    db = connect()
    c = db.cursor()
    #creamos sentencia para insertar datos
    query = """DELETE FROM `cars` where id = %s"""
    data = [(id)]
    #ejecutamos el query
    c.execute(query, data)
    #hacemos commit del cambio en db
    db.commit()
    db.close()