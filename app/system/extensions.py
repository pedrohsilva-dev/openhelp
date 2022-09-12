from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# instances managers
db = SQLAlchemy()


class configEngine:
    def __init__(self, config=None) -> None:
        self.config = config

    def init_app(self, config):
        self.config = config


config = configEngine()
# factory extensions


def init_app(server=None):
    # start instance Database Manager
    db.init_app(server)
    config.init_app(server.config)
    # Notice that we are passing in the actual sqlalchemy user object here
    Migrate(server, db)
