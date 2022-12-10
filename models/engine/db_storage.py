#!/usr/bin/python3
"""This defines the DBStorage class"""

import os
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv


user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
database = os.getenv('HBNB_MYSQL_DB')

classes = {'User': User,
           'State': State,
           'City': City,
           'Amenity': Amenity,
           'Place': Place,
           'Review': Review}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'db':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict_1 = {}
        if cls is None:
            for value in classes.values():
                state_info = self.__session.query(value)
                for obj in state_info:
                    key = obj.__class__.__name__ + "." + obj.id
                    dict_1[key] = obj
        else:
            state_info = self.__session.query(classes[cls])
            for obj in state_info:
                key = obj.__class__.__name__ + "." + obj.id
                dict_1[key] = obj
        return dict_1

    def new(self, obj):
        '''new obj added to the session'''
        self.__session.add(obj)

    def save(self):
        '''save obj'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete obj'''
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session1 = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session2 = scoped_session(Session1)
        self.__session = Session2()

    def close(self):
        """calls the methos remove()"""
        self.__session.close()
