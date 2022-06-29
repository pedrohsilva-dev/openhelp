from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


def init_app(server=None):
    db.init_app(server)
    Migrate(server, db)
