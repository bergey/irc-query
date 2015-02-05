from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tables import *

import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello You!'

@app.route('/json')
def json_demo():
    return json.dumps(['Hello', 'World'])

# setup DB session
# TODO worry about threads & scope
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/v1/presence')
def all_presences():
    return json.dumps(session.query(Presence).all(), cls=SqlJson)

@app.route('/v1/channel/<c>')
def channel_presence(c):
    return json.dumps([p.user_name for p in session.query(Presence).filter(Presence.channel == c).all()], cls=SqlJson)

@app.route('/v1/user/<u>')
def user_presence(u):
    return json.dumps([p.channel for p in session.query(Presence).filter(Presence.user_name == u).all()], cls= SqlJson)

if __name__ == '__main__':
    app.run(debug=True)
