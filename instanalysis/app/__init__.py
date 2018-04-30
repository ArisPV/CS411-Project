from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_object('config')

app.config['MONGO_DBNAME'] = 'dounut'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/dounut'
app.config['MONGO_URI'] = 'mongodb://lijun:411@ds263089.mlab.com:63089/donut'

from app import routes