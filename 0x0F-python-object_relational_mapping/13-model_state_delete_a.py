#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database using SQLAlchemy.
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

    # Query and retrieve all State objects with 'a' in the name
    states_to_delete = session.query(State).filter(
		    State.name.like('%a%')).all()

    # Delete the retrieved State objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
