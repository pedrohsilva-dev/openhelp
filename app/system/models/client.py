from app.system.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


# const companies = await axios.get("/api/companies")
# const name_company = companies.data["company_name"]
# <View><Text>{name_company}</Text></View>

class Client(db.Model):
    # nomeia como 'client' a tabela no banco
    __tablename__ = "client"

    # cria campo chave primaria
    id = db.Column(db.Integer, primary_key=True)

    # cria campos username, email, password, city, state
    username = db.Column(db.String)
    # o campo unique diz que não deve existir dois dados com mesmo valor neste campo da tabela
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    photo_profile = db.Column(db.String(125))

    def __init__(self, username: str, email: str, password: str, city: str, state: str, photo_profile: str):
        self.username = username.strip()
        self.email = email.lower().strip()

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

    def update_client(self, args):

        username = args.get("username")
        email = args.get("email")
        password = args.get("password")
        city = args.get("city")
        state = args.get("state")

        if username != None:
            self.username = username
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
    def find(cls, client_id):
        client = cls.query.filter_by(id=client_id).first()
        return client

    @classmethod
    def sign(cls, email: str, password: str):
        client = cls.query.filter_by(email=email).first()

        if check_password_hash(client.password,  password) == True:
            user = cls(
                username=client.username,
                email=client.email,
                city=client.city,
                state=client.state,
                password="",
                photo_profile=client.photo_profile
            )

            user.id = client.id
            return user
        return None

    def __repr__(self) -> str:
        return f"""
        Client<ID: {self.id}, USERNAME: {self.username}>
        """
