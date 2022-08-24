from app.extensions import db
from werkzeug.security import generate_password_hash


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.String)
    cnpj = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    photo_profile = db.Column(db.String(125))

    def __init__(self, company_name: str, email: str, password: str, city: str, state: str, photo_profile: str):
        self.company_name = company_name

        self.email = email
        self.password = generate_password_hash(password)

        self.city = city.lower()
        self.state = state.strip()
        self.photo_profile = photo_profile

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete_object(self):
        db.session.delete(self)
        db.session.commit()

    def update_company(self, args):

        company_name = args.get("company_name")

        email = args.get("email")
        password = args.get("password")

        city = args.get("city")
        state = args.get("state")

        if company_name != None:
            self.company_name = company_name
        if email != None:
            self.email = email
        if password != None:
            self.password = password

        if city != None:
            self.city = city
        if state != None:
            self.state = state
        db.session.commit()

    @classmethod
    def getAll(cls, page=None, city="são miguel arcanjo", state="SP"):
        return cls.query.filter_by(city=city, state=state).paginate(page=page, per_page=5).items

    @classmethod
    def find(cls, company_id):
        company = cls.query.filter_by(id=company_id).first()
        return company

    def __repr__(self) -> str:
        return f"""
        Company<ID: {self.id}, Company name: {self.company_name}>
        """
