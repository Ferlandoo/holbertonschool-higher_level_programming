#!/usr/bin/python3
"""List all states from the database hbtn_0e_0_usa."""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[0], argv[1], argv[2]))
Base.metadata.create_all(engine)
session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()