from datetime import datetime, timezone
from app.system.extensions import db


class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    type_user = db.Column(db.Integer)
    origin = db.Column(db.String)
    destination = db.Column(db.String)
    date_time = db.Column(db.String)

    def __init__(self, title: str, content: str, origin: str, destination: str, typeUser: str):
        self.title = title
        self.content = content
        self.origin_user = origin
        self.destination_user = destination
        self.type_user = typeUser
        self.date_time = "2012-08-01"

    def save(self, object):
        db.session.add(self)
        db.session.commit()
