from app.system.extensions import db


class Follow(db.Model):
    __tablename__ = "follows"

    id = db.Column(db.Integer, primary_key=True)

    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    client = db.relationship("Client", foreign_keys=client_id)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    company = db.relationship("Company", foreign_keys=company_id)

    def __init__(self, client_id, company_id):
        self.client_id = client_id
        self.company_id = company_id

    def save(self):
        db.session.add(self)
        db.session.commit()
