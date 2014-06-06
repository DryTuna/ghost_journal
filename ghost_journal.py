# -*- coding: utf-8 -*-

from flask import Flask
from contextlib import closing

import os
import psycopg2

DB_SCHEMA = """
DROP TABLE IF EXISTS stories;
CREATE TABLE stories (
    id serial PRIMARY KEY,
    title VARCHAR (127) NOT NULL,
    author VARCHAR (127) NOT NULL,
    text TEXT NOT NULL,
    created TIMESTAMP NOT NULL
    )
"""

app = Flask(__name__)

app.config['DATABASE'] = os.environ.get(
    'dbname=ghost_journal user=drytuna'
    )

@app.route('/')
def ghost_stories():
    return u'Welcome to Ghost Journal'

def connect_db():
    return psycopg2.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        db.cursor().execute(DB_SCHEMA)
        db.commit()

if __name__ == '__main__':
    app.run(debug = True)