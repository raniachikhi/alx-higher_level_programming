#!/usr/bin/python3
"""
This module defines the State class, which represents a state in a database.
"""

from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
        cities (relationship): A relationship to the City class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
