#!/usr/bin/python3
"""
Script that changes the name of a State object in the database
using SQLAlchemy.
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

    # Query and retrieve the State object with the ID '2'
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Change the name of the State object
        state_to_update.name = "New Mexico"

        # Commit the changes to the database
        session.commit()
    else:
        print("State with ID '2' not found")

    # Close the session
    session.close()
