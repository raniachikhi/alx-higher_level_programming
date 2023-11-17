#!/usr/bin/python3
"""
This module performs MySQL queries using SQLAlchemy to retrieve
City objects
along with their corresponding State objects.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for a_city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(a_city.id, a_city.name, a_city.state.name))

    session.close()
