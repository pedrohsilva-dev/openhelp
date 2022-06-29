from flask import request
from flask_restful import Resource

from app.repositories.users import UserRepository


class ClientResource(Resource):

    def __init__(self):
        self.repository = UserRepository()

    def get(self):
        return self.repository.all()

    def post(self):
        return self.repository.insert(request.data)

    def put(self, client_id):
        return self.repository.update(client_id, request.data)

    def patch(self):
        ...

    def delete(self, client_id):
        return self.repository.destroy(client_id)
