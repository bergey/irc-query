from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Presence, engine

import itertools
import os

# Connect to DB
DBSession = sessionmaker(bind=engine)
session = DBSession()

fake_data = {
    'diagrams': ['bergey', 'byorgey', 'martingale'],
    'haskell': ['bergey', 'edwardk', 'jwiegley'],
    'nixos': ['jwiegley', 'ocharles', 'fuuzetsu']
}

def insert_presence(ds):
    presences = [[Presence(channel=c, user_name=n) for n in ns] for c, ns in ds.items()]
    for p in itertools.chain(*presences):
        session.add(p)
    session.commit()

if len(session.query(Presence).all()) == 0:
    insert_presence(fake_data)
