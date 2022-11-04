import os
from flask import Response, make_response, request, send_from_directory
from flask_restful import Resource, abort, marshal, marshal_with, reqparse, fields, representations
from app.system.models.company import Company
from app.system.models.warning import Warnings
from app.system.services.lib_jwt import auth_jwt_required

parserWarning = reqparse.RequestParser()

# id = db.Column(db.Integer, primary_key=True)
# title = db.Column(db.String)
# content = db.Column(db.String)
# image = db.Column(db.String)
# company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))

parserWarning.add_argument("per_page", type=int, location="args")
parserWarning.add_argument("page", type=int, location="args")

resource_fields_company = {
    "id": fields.Integer(),
    "company_name": fields.String(),
    "email": fields.String(),
    "city": fields.String(),
    "state": fields.String(),
}

response_marshal = {
    "id": fields.Integer,
    "title": fields.String,
    "content": fields.String,
    "image": fields.String,
    "company": fields.Nested(resource_fields_company)
}


class WarningResource(Resource):
    @auth_jwt_required
    @marshal_with(response_marshal)
    def get(self, current_user):
        args = parserWarning.parse_args(request)

        page = int(args.get("page", None))
        per_page = int(args.get("per_page", None))
        data = list()
        warnings = Warnings.getAll(
            page, per_page, client_id=current_user.id)

        for i in warnings:
            data.append({
                "id": int(i.id),
                "title": str(i.title),
                "content": str(i.content),
                "image": "/warnings/image/" + str(i.id),
                "company": marshal(i.company, resource_fields_company)
            })
        return data
