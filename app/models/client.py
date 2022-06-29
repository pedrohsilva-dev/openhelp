from app.extensions import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name.strip()
        self.email = email.lower().strip()
        self.password = hash(password)
