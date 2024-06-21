from db.database import connect
from openpyxl import Workbook

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
    c = db.cursor(dictionary=True)
    #creamos sentencia para insertar datos
    query = """SELECT * FROM `cars` INNER JOIN brands ON cars.brand_id = brands.id where id = %s"""
    data = [(id)]
    #ejecutamos el query
    c.execute(query, data)
    car = c.fetchone()
    db.close()
    return car

def get_all_car():
    #conexion con base de datos
    db = connect()
    c = db.cursor(dictionary=True)
    #creamos sentencia para insertar datos
    query = """SELECT * FROM `cars` INNER JOIN brands ON cars.brand_id = brands.id"""
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

def export_car_to_excel(cars):
    #inicializa la libreria
    wb = Workbook()
    #obtiene el worksheet activo
    ws = wb.active
    #agregamos la cabecera
    ws.append(["marca", "modelo", "color"])
    #agregamos los datos del auto
    for car in cars:
        ws.append([car['name'], car['model'], car['color']])
    wb.save("cars.xlsx")