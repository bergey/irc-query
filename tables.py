from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Presence(Base):
    __tablename__ = 'presence'
    id = Column(Integer, primary_key=True)
    channel = Column(Text, nullable=False)
    user_name = Column(Text, nullable=False)

engine = create_engine('postgresql://bergey:password@localhost')

Base.metadata.create_all(engine)
