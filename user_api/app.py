from flask import Flask 
from models import db

app = Flask(__name__)

app.config(dict(
    SECRET_KEY='SECRET',
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@localhost/order'
))

db.init_app(app)