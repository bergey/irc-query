from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import json

import os

Base = declarative_base()

class Presence(Base):
    __tablename__ = 'presence'
    id = Column(Integer, primary_key=True)
    channel = Column(Text, nullable=False)
    user_name = Column(Text, nullable=False)

    def _json_enc(self):
        return { 'channel': self.channel, 'user_name': self.user_name }

# Connect to DB
engine = create_engine(os.environ['DATABASE_URL'])

Base.metadata.create_all(engine)

# All classes inheriting from Base should also be serializable to JSON
# It is sufficient to add a _json_enc method to each class, and use the
# Encoder below
class SqlJson(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, '_json_enc') and callable(o._json_enc):
            return o._json_enc()
        return json.JSONEncoder.default(self, o)
