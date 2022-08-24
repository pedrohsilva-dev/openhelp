from flask import Flask
from flask_jwt_extended import JWTManager

from app.models.client import Client
# configuration JWT
jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Client.query.filter_by(id=identity).one_or_none()


def init_app(server: Flask):
    jwt.init_app(server)
