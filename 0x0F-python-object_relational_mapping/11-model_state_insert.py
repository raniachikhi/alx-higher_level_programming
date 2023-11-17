#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database
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

    # Create and add the State object "Louisiana"
    add_state = State(name="Louisiana")
    session.add(add_state)

    # Commit the changes to the database
    session.commit()

    # Print the ID of the added State object
    print(add_state.id)

    # Close the session
    session.close()
