from typing import Dict
from flask_restful import fields, marshal_with, Resour


class ClientData():
    def __init__(self):
        self.resource_fields = {
            "id": fields.Integer,
            "username": fields.String(),
            "email": fields.String(),
            "password": fields.String(),
            "city": fields.String(),
            "state": fields.String(),
            "country": fields.String(),
        }

    def serialize(self, obj: Dict):
        return marshal_with(self.resource_fields)
