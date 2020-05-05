from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db

def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.netadata.create_all(engine)
    return engine

