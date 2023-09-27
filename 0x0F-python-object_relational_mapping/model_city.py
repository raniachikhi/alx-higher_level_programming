#!/usr/bin/python3
"""
This module defines the City class, which represents a city in
a database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that inherits from Base.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The foreign key linking the city to a state.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
