from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import json

Base = declarative_base()

class Presence(Base):
    __tablename__ = 'presence'
    id = Column(Integer, primary_key=True)
    channel = Column(Text, nullable=False)
    user_name = Column(Text, nullable=False)

    def _json_enc(self):
        return { 'channel': self.channel, 'user_name': self.user_name }

engine = create_engine('postgresql://bergey:password@localhost')

Base.metadata.create_all(engine)

class SqlJson(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, '_json_enc') and callable(o._json_enc):
            return o._json_enc()
        return json.JSONEncoder.default(self, o)
