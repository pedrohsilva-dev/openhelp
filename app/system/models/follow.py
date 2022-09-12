from app.system.extensions import db


class Follow(db.Model):
    __tablename__ = "follow"
    id = db.Column(db.IUnteger, primary_key=True)
    client = db.Column(db.IUnteger, primary_key=True)
    client = db.Column(db.IUnteger, primary_key=True)
