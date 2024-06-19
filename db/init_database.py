from db.database import connect

def create_database():
    #conexion con base de datos
    db = connect()
    c = db.cursor()
    #crear tabla de marcas (brands)
    query = """CREATE TABLE IF NOT EXISTS `brands` (
              `id` INT NOT NULL AUTO_INCREMENT,
              `name` VARCHAR(45) NOT NULL,
               PRIMARY KEY (`id`))"""
    c.execute(query)
    c = db.cursor()
    # verificar que quede bien la tabla
    print("table brands")
    c.execute("desc brands")
    for i in c:
        print(i)
    c = db.cursor()
    #crear tabla de autos (cars)
    query = """CREATE TABLE IF NOT EXISTS `cars` (
              `id` INT NOT NULL AUTO_INCREMENT,
              `brand_id` INT NOT NULL,
              `model` VARCHAR(45) NOT NULL,
              `color` VARCHAR(45) NOT NULL,
               PRIMARY KEY (`id`))"""
    c.execute(query)
    c = db.cursor()
    # verificar que quede bien la tabla
    print("table cars")
    c.execute("desc cars")
    for i in c:
        print(i)
    # finally closing the database connection
    c = db.cursor()
    db.close()

def add_initial_brands():
    #conexion con base de datos
    db = connect()
    c = db.cursor()
    #creamos sentencia para insertar datos
    query = """INSERT INTO `brands` (name) VALUES(%s)"""
    #creamos una lista con los autos a crear
    data = [
        ["chevrolet"],
        ["ford"],
        ["ferrary"],
    ]
    #insertamos los datos
    c.executemany(query, data)
    db.commit()
    db.close()

def fresh():
    #conexion con base de datos
    db = connect()
    c = db.cursor()
    #limpiamos las tablas
    c.execute("truncate cars")
    c.execute("truncate brands")
    db.commit()
    db.close()