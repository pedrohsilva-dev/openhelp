from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.models.company import Company

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return Company.get(user_id)

def init_app(server=None):
    db.init_app(server)server
	login_manager.init_app(server)
    # Notice that we are passing in the actual sqlalchemy user object here

    Migrate(server, db)
