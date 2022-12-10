#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.base_model import BaseModel
from models.amenity import Amenity
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from .engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review,
           "State": State, "User": User}


storage.reload()
