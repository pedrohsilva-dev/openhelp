import os
from time import sleep
from flask import jsonify, request
from flask_restful import Resource, fields, marshal_with, reqparse
import werkzeug
from app.models.client import Client

resource_fields = {
    "id": fields.Integer(),
    "username": fields.String(),
    "email": fields.String(),
    "city": fields.String(),
    "state": fields.String(),
    "photo_profile": fields.String()
}
parser = reqparse.RequestParser()
parser.add_argument('username', location="form")
parser.add_argument('email', location="form")
parser.add_argument('password', location="form")
parser.add_argument('city', location="form")
parser.add_argument('state', location="form")
parser.add_argument(
    "photo_profile", type=werkzeug.datastructures.FileStorage, location='files'
)


class ClientResource(Resource):

    def __init__(self):
        ...

    @marshal_with(resource_fields)
    def get(self):
        return Client.getAll(), 200

    @marshal_with(resource_fields, "client")
    def post(self):
        args = parser.parse_args(request)

        username = args.get("username")
        email = args.get("email")
        password = args.get("password")
        city = args.get("city")
        state = args.get("state")

        photo_profile = args.get("photo_profile")

        filename = photo_profile.filename

        print(photo_profile.save(os.path.join(os.path.abspath("files"), filename)))

        client = Client(username, email, password, city,
                        state, filename)

        client.save()

        return client, 200

    def put(self, client_id):
        args = parser.parse_args(request)

        client: Client = Client.query.filter_by(id=int(client_id))

        username = args.get("username")
        email = args.get("email")
        password = args.get("password")
        city = args.get("city")
        state = args.get("state")

        new_object = dict()

        if username != None:
            new_object["username"] = username
        if email != None:
            new_object["email"] = email
        if password != None:
            new_object["password"] = password
        if city != None:
            new_object["city"] = city
        if state != None:
            new_object["state"] = state

        client.update_object(new_object)

        return client

    def patch(self):
        args = parser.parse_args(request)

        client: Client = Client.query.filter_by(id=int(client_id))

        username = args.get("username")
        email = args.get("email")
        password = args.get("password")
        city = args.get("city")
        state = args.get("state")

        new_object = dict()

        new_object["username"] = username
        new_object["email"] = email
        new_object["password"] = password
        new_object["city"] = city
        new_object["state"] = state

        client.update_object(new_object)

        return client

    def delete(self, client_id):

        client: Client = Client.query.filter_by(id=int(client_id))

        client.delete_object()
        return client_id
