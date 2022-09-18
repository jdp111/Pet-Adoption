from email.policy import default
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """creates pets"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text)
    species = db.Column(db.Text)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default = True)