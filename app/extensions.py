from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


def init_app(server=None):
    db.init_app(server)

    # Notice that we are passing in the actual sqlalchemy user object here

    Migrate(server, db)
