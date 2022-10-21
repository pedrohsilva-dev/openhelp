from app.system.extensions import db
from sqlalchemy import select

from app.system.models.company import Company
from app.system.models.follow import Follow


class Warnings(db.Model):
    __tablename__ = "warnings"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    image = db.Column(db.String)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    company = db.relationship(
        "Company", foreign_keys=company_id)

    def __init__(self, title: str, content: str, image: str, company_id: int):
        self.title = title
        self.content = content
        self.image = image
        self.company_id = company_id

    @classmethod
    def getAll(cls, page: int = None, per_page: int = None, client_id=None):

        warnings = Warnings.query.filter(
            Follow.client_id == client_id
        ).order_by('title')
        qtd_min = (per_page * page) - per_page
        qtd_max = (per_page * page)
        return warnings.all()[qtd_min:qtd_max]

    def save(self):
        db.session.add(self)
        db.session.commit()
