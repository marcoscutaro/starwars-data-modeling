import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Characters (Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    favorite_character = relationship("Favorite")


class Planets (Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    diameter = Column(String(250))
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    population = Column(String(250))
    favorite_planet = relationship("Favorite")

class Starships (Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    diameter = Column(String(250))
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    population = Column(String(250))
    favorite_planet = relationship("Favorite")


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_fav = Column(Integer,ForeignKey('character.id'))
    character_relation = relationship ('Character', back_populates = 'favorite_character')
    planet_fav = Column(Integer,ForeignKey('planet.id'))
    planet_relation = relationship ('Planet', back_populates = 'favorite_planet')
    starships_fav = Column(Integer,ForeignKey('planet.id'))
    starships_relation = relationship ('Starships', back_populates = 'favorite_starships')







    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
