from flask import Flask

# from flask_jwt_extended import JWTManager
from flask_login import LoginManager

# from app.system.models.client import Client
from app.system.models.company import Company


# # configuration JWT
# jwt = JWTManager()
login_manager = LoginManager()

login_manager.login_view = "loginView"


# @jwt.user_identity_loader
# def user_identity_lookup(user):
#     return user.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
# @jwt.user_lookup_loader
# def user_lookup_callback(_jwt_header, jwt_data):
#     identity = jwt_data["sub"]
#     return Client.query.filter_by(id=identity).one_or_none()


@login_manager.user_loader
def load_user(id):
    return Company.query.filter_by(id=id).first()


def init_app(server: Flask):
    # jwt.init_app(server)
    login_manager.init_app(server)
