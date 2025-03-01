import pathlib

from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
DB_LOCATION = BASE_DIR / 'instance' / 'db.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_LOCATION}'
app.config['SECRET_KEY'] = 'SUPER SECRET KEY'
db = SQLAlchemy(app)

from . import api, views