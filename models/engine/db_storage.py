#!/usr/bin/python3
"""This defines the DBStorage class"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
database = os.getenv('HBNB_MYSQL_DB')

classes = {
    'City': City,
    'User': User,
    'Review': Review,
    'State': State,
    'Place': Place,
    'Amenity': Amenity
    }


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user, password, host, database
                ),
            pool_pre_ping=True
            )

        if os.getenv("HBNB_ENV ") == 'test':
            meta = MetaData(self.__engine)
            meta.drop_all()

    def all(self, cls=None):
        dic = {}
        if not cls:
            for actual_class in classes.values():
                object_list = self.__session.query(actual_class).all()
                for obj in object_list:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dic[key] = obj
        else:
            object_list = self.__session.query(cls).all()
            for obj in object_list:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dic[key] = obj
        return dic

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(expire_on_commit=False, bind=self.__engine)
        Scoped = scoped_session(Session)
        self.__session = Scoped

    def close(self):
        """remove method on private session attribute"""
        self.__session.remove()
