from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Presence

import itertools

engine = create_engine('postgresql://bergey:password@localhost')
Base.metadata.bind = engine

fake_data = {
    '#diagrams': ['bergey', 'byorgey', 'martingale'],
    '#haskell': ['bergey', 'edwardk', 'jwiegley'],
    '#nixos': ['jwiegley', 'ocharles', 'fuuzetsu']
}

DBSession = sessionmaker(bind=engine)
session = DBSession()

presences = [[Presence(channel=c, user_name=n) for n in ns] for c, ns in fake_data.items()]
for p in itertools.chain(*presences):
    session.add(p)

session.commit()
