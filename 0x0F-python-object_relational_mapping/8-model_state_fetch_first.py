#!/usr/bin/python3
"""
Script that prints the first State object from the database
using the SQLAlchemy module.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a Session class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create database tables based on the models
    Base.metadata.create_all(engine)

    # Query and retrieve the first State object ordered by ID
    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
