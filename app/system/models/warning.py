from app.system.extensions import db


class Warnings(db.Model):
    __tablename__ = "warning"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    image = db.Column(db.String)

    def __init__(self, title: str, content: str, image: str):
        self.title = title
        self.content = content
        self.image = image

    def save(self):
        db.session.add(self)
        db.session.commit()
