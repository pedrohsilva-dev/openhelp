from http import client
from flask import current_app, request
from flask_restful import Resource, marshal, marshal_with, reqparse, fields, abort

from app.system.models.client import Client
from app.system.services.lib_jwt import generate_token, auth_jwt_required


resource_fields_client = {
    "id": fields.Integer(),
    "username": fields.String(),
    "email": fields.String(),
    "city": fields.String(),
    "state": fields.String(),
}

# resposta vai ser no formato abaixo
resource_fields_token = {
    "token": fields.String(),
    "client": fields.to_marshallable_type(resource_fields_client)
}


# request de validação do formulario api de envio
parserLogin = reqparse.RequestParser()
parserLogin.add_argument('email')
parserLogin.add_argument('password')


class Login(Resource):
    def post(self):
        """Login"""
        args = parserLogin.parse_args(request)

        email: str = args.get("email")
        password: str = args.get("password")

        user = Client.sign(email, password)

        if (user != None):

            token = generate_token(
                user.id, current_app.config["SECRET_KEY"], 120)
            return {"token": token, "client": marshal(user, resource_fields_client)}
        return abort(404)

    @auth_jwt_required
    @marshal_with(fields=resource_fields_client, envelope="data")
    def get(self, current_user):
        result = {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "city": current_user.city,
            "state": current_user.state,
            "photo_profile": current_user.photo_profile
        }

        return result, 200
