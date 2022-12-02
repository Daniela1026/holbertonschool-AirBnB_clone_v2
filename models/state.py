#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states')
    else:
        @property
        def cities(self):
            """ Getter attribute cities """
            from models import storage
            from models.city import City
            list = []
            cities = storage.all(City)
            for value in cities.values():
                if value.state_id == self.id:
                    list.append(value)
            return list
