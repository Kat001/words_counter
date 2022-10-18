from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from rq import Queue

# from models import UrlWordsCount

app = Flask(__name__)

# Async call setup...
redis = Redis()
queue = Queue(connection=redis)

db = SQLAlchemy()
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from words_scrapper import views
