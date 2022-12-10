#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base if HBNB_TYPE_STORAGE == 'db' else object):
    """ State class """
    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state",
            cascade="all, delete, delete-orphan"
        )
    else:
        name = ""

    if HBNB_TYPE_STORAGE != 'db':
        @property
        def cities(self):
            from models.city import City
            from models import storage
            ls = []
            objects_cities = storage.all(City)
            for city in objects_cities.values():
                if city.state_id == self.id:
                    ls.append(city)
            return ls
