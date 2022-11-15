from app.system.extensions import db

from app.system.models.follow import Follow
from app.system.models.client import Client
from datetime import datetime


class Warnings(db.Model):
    __tablename__ = "warnings"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    image = db.Column(db.String)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    company = db.relationship(
        "Company", foreign_keys=company_id)
    pub_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow)

    def __init__(self, title: str, content: str, image: str, company_id: int):
        self.title = title
        self.content = content
        self.image = image
        self.company_id = company_id

    @classmethod
    def getAll(cls, page: int = None, per_page: int = None, client_id=None):
        qtd_min = (per_page * page) - per_page
        qtd_max = (per_page * page)
        data = Warnings.query.select_from(Follow).join(Client).filter(
            Warnings.company_id == Follow.company_id).filter(Client.id == client_id).order_by(Warnings.id).all()

        return data[qtd_min:qtd_max]

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
