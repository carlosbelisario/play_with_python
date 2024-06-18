from peewee import *
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE = os.getenv('DATABASE')
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class Brand(BaseModel):
    name = CharField()

class Car(BaseModel):
    brand = ForeignKeyField(Brand)
    model = CharField()
    color = CharField()