#!/usr/bin/python3
"""Lists all State objects that contain the letter a."""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = session.query(State).order_by(State.id).filter(State.name == "%a%").all()
    if query is None:
        print("Nothing")
    else:
        for element in query:
            print(f"{query.id}: {query.name}")
    session.close()
