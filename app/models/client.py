
from typing import Dict
from app.extensions import db
from werkzeug.security import generate_password_hash


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    photo_profile = db.Column(db.String(125))

    def __init__(self, username: str, email: str, password: str, city: str, state: str, photo_profile: str):
        self.username = username.strip()
        self.email = email.lower().strip()

        self.password = generate_password_hash(password)

        self.city = city.lower()
        self.state = state.strip()
        self.photo_profile = photo_profile

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_object(self):
        db.session.delete(self)
        db.session.commit()

    def update_object(self, data: Dict):
        self.update(data)
        db.session.commit()

    @classmethod
    def getAll(cls):
        return cls.query.all()
