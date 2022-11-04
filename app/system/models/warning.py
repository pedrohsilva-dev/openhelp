from app.system.extensions import db

from app.system.models.follow import Follow
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
        follows = Follow.query.filter_by(client_id=client_id).all()
        data = []
        for i in follows:
            data.append(Warnings.query.filter_by(
                company_id=i.company_id).first())

        qtd_min = (per_page * page) - per_page
        qtd_max = (per_page * page)
        return data[qtd_min:qtd_max]

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
