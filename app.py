import os
from dotenv import load_dotenv
load_dotenv()
from models import *

#get first brand "chevrolet" by migration potition
brand = Brand.get(Brand.id == 1)
#create a car
Car = Car.create(brand = brand, model = 'cruze', color = 'red')