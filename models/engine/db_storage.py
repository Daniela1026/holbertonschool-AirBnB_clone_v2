#!/usr/bin/python3
"""This defines the DBStorage class"""

from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from os import environ


class DBStorage():
    """Defines the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """
        Starting the engine
        """
        user = environ('HBNB_MYSQL_USER')
        pwd = environ('HBNB_MYSQL_PWD')
        host = environ('HBNB_MYSQL_HOST')
        database = environ('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, database),
                                      pool_pre_ping=True)
        if environ('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Perform query on the current database session
        """
        obj_dict = {}
        if cls != '':
            objs = self.__session.query(cls)
        else:
            objs = self.__session.query(Amenity)
            objs += self.__session.query(City)
            objs += self.__session.query(Place)
            objs += self.__session.query(Review)
            objs += self.__session.query(State)
            objs += self.__session.query(User)
        return {"{}.{}".format(obj.__class__.__name__, obj.id): obj
                for obj in objs}

    def new(self, obj):
        """Adds the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to current db session"""
        self.__session.commit()

    def delete(self, obj):
        """ Delete obj of current db session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Commit all changes in database after
        the changings
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """close session, proper ending"""
        self.__session.remove()

    def classes(self):
        """ returns dictionary of valid classes """
