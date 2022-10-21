from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

import werkzeug
from werkzeug.utils import secure_filename

from app.system.models.client import Client
from app.website.utils import dir_file, generate_namefile


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
        "photo_profile", type=werkzeug.datastructures.FileStorage, location='form'
    )
# 192.168.10.102
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
        photo_profile = request.files.get("photo_profile")

        filename_photo = generate_namefile(
            secure_filename(photo_profile.filename), photo_profile.content_type
        )
        photo_profile.save(dir_file(filename_photo))

        # salva cliente
        try:
            client = Client(username, email, password, city,
                            state, filename_photo)
            if (client != None):
                client.save()

                return client, 200
        except Exception as ex:
            return None, 505

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
