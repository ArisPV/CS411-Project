from flask import Flask

from flask_pymongo import PyMongo
import flask_pymongo


app = Flask(__name__)
mongo = PyMongo(app)
app.config.from_object('config')

from app import routes




