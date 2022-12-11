#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os
from models.review import Review

metadata = Base.metadata
place_amenity = Table(
    'place_amenity',
    metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False),
    extend_existing=True)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            from models import storage
            return [review for review in list(storage.all(Review).values())
                    if review.place_id == self.id]

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            return [amenity for amenity in list(storage.all(Amenity).values())
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            if obj is not None:
                self.amenity_ids.append(obj.id)
