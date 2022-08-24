from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

import werkzeug

from app.models.client import Client


def client_request_response():
    # resposta vai ser no formato abaixo
    resource_fields = {
        "id": fields.Integer(),
        "username": fields.String(),
        "email": fields.String(),
        "city": fields.String(),
        "state": fields.String(),
        "photo_profile": fields.String()
    }
    # request de validação do formulario api de envio
    parser = reqparse.RequestParser()
    parser.add_argument('username', location="form")
    parser.add_argument('email', location="form")
    parser.add_argument('password', location="form")
    parser.add_argument('city', location="form")
    parser.add_argument('state', location="form")
    parser.add_argument(
        "photo_profile", type=werkzeug.datastructures.FileStorage, location='files'
    )

    return {
        "parser": parser,
        "resource": resource_fields
    }


resource_field_client = client_request_response()['resource']
parser_client = client_request_response()['parser']

# requisição de paginação
parser_get_pagination = reqparse.RequestParser()
parser_get_pagination.add_argument("page", type=int, location="args")


class ClientResource(Resource):

    def __init__(self):
        ...

    @marshal_with(resource_field_client)
    def get(self, client_id=None):
        if client_id == None:
            args = parser_get_pagination.parse_args(request)
            requerystr = args.get("page")

            return Client.getAll(page=requerystr), 200
        else:
            return Client.find(client_id=client_id), 200

    @marshal_with(resource_field_client, "client")
    def post(self):
        args = parser_client.parse_args(request)
        # get values client
        username = args.get("username")
        email = args.get("email")
        password = args.get("password")
        city = args.get("city")
        state = args.get("state")
        # photo client
        photo_profile = args.get("photo_profile")

        filename = photo_profile.filename

        # salva cliente
        client = Client(username, email, password, city,
                        state, filename)

        client.save()

        return client, 200

    @marshal_with(resource_field_client)
    def patch(self, client_id):
        args = parser_client.parse_args(request)

        client = Client.find(client_id=client_id)
        # atualiza cliente
        client.update_client(args)

        return client

    def delete(self, client_id):

        client: Client = Client.query.filter_by(id=int(client_id))
        # deleta cliente
        client.delete_object()
        return client_id
