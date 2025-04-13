# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime,timezone

class movie(db.Model):
    __tablename__ = 'movies'

    id= db.Column(db.Integer, primary_key = True)
    movietitle= db.Column(db.String(150))
    description = db.Column(db.String(250))
    poster= db.Column(db.String(300))
    created_at= db.Column(db.DateTime, default=datetime.now(timezone.utc))
