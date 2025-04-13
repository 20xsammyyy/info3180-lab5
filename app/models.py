from app import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'  # Explicitly set the table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Title can't be empty
    description = db.Column(db.Text, nullable=False)  # Description can't be empty
    poster = db.Column(db.String(255), nullable=False)  # Poster filename can't be empty
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Movie {self.title}>"
