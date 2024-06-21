from functions import *

#create_car(brand=1, model='cruze', color='rojo') agrega un nuevo auto a la base de datos
# print(get_car(id=1)) lista un auto por id
# print(get_all_car()) lista todos los autos disponibles
#delete_car(id=1) elimina un auto de la base de datos por id

#ejemplo excel
#lista con los autos
cars = get_all_car()
#le pasamos a la funcion de exportar la lista de autos
export_car_to_excel(cars)