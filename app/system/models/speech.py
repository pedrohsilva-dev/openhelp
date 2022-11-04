from app.system.extensions import db
from sqlalchemy import Integer, Column, ForeignKey, select


class Speech(db.Model):
    __tablename__ = "speeches"

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey("messages.id"))
    message = db.relationship(
        "Message", foreign_keys=message_id, backref='speeches', lazy=True)
    follow_id = Column(Integer, ForeignKey("follows.id"))
    follow = db.relationship(
        "Follow", foreign_keys=follow_id)

    def __init__(self, follow_id: int, message_id: int):
        self.follow_id = follow_id
        self.message_id = message_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def list_message_follow(cls, follow_id):
        result = db.session.execute(
            select(cls).where(cls.follow_id == int(follow_id))
        ).scalar()
        return result

    @classmethod
    def list_messages(cls, follow_id):
        result = db.session.execute(
            select(cls).where(cls.follow_id == int(follow_id))
        ).scalars()
        return result
