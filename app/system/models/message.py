from datetime import datetime, timezone
from app.system.extensions import db


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    who = db.Column(db.String)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    def __init__(self, title: str, content: str, who: str):
        self.title = title
        self.content = content
        self.who = who

    def save(self):
        db.session.add(self)
        db.session.commit()
