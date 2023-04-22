from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    waist = db.Column(db.Float, nullable=False)
