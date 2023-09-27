#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an
argument from the database using SQLAlchemy.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create database tables based on the models
    Base.metadata.create_all(engine)

    # Query and retrieve the State object with the provided name
    state = session.query(State).filter(State.name == argv[4]).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
