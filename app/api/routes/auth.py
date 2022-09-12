
import datetime
from flask_restful import Resource, reqparse, fields, marshal_with
from flask_jwt_extended import jwt_required, create_access_token

from app.system.models.client import Client


def auth_request_response():
    # resposta vai ser no formato abaixo
    resource_fields = {
        "id": fields.Integer(),
        "company_name": fields.String(),
        "email": fields.String(),
        "city": fields.String(),
        "state": fields.String(),
        "photo_profile": fields.String()
    }
    # request de validação do formulario api de envio
    parser = reqparse.RequestParser()
    parser.add_argument('email')
    parser.add_argument('password')

    return {
        "parser": parser,
        "resource": resource_fields
    }


parserLogin: reqparse.RequestParser = auth_request_response()["parser"]
resourceLogin = auth_request_response()["resource"]
res = {
    "token": fields.String,
    "expire": fields.Float
}


class Login(Resource):
    @marshal_with(res)
    def post(self):
        """Login"""
        args = parserLogin.parse_args()

        email: str = args.get("email")
        password: str = args.get("password")

        user = Client.sign(email, password)

        if (user != None):

            token = create_access_token(
                user
            )
            return {"token": token, "expire": 0.0}
        else:
            return None, 404

    @jwt_required
    def get(self):
        return "Bearer token: dwjdbfhuihdfi9dshfoidsjfjdsoifjsdiofjidsjf"
