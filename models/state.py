#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if environ('HBNB_TYPE_STORAGE') == 'db':
        """ db ==>  means let's go for SQLAlchemy logic"""
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

    @property
    def cities(self):
        """
        Getter - returns the list of City instances
        """
        l_cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                l_cities.append(city)
        return l_cities
