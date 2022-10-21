from flask import request
from flask_restful import Resource, marshal, reqparse, marshal_with, fields

from app.system.models.follow import Follow
from app.system.models.company import Company
from app.system.services.lib_jwt import auth_jwt_required

parser_warning = reqparse.RequestParser()
parser_warning.add_argument('company_id', type=int)

parser_search_company = reqparse.RequestParser()
parser_search_company.add_argument('csearch', type=str, location="args")


resource_fields_follow_company = {
    "id": fields.Integer(),
    "company_name": fields.String(),
    "email": fields.String(),
    "city": fields.String(),
    "state": fields.String(),
    "photo_profile": fields.String()
}

resource_fields = {
    "id": fields.Integer(),
    "company": fields.Nested(resource_fields_follow_company)
}


class FollowResource(Resource):
    @auth_jwt_required
    @marshal_with(resource_fields)
    def post(self, current_user):
        args = parser_warning.parse_args(request)
        client_id = int(current_user.id)
        company_id = int(args.get("company_id"))
        # print(f"Client: {client_id}\nCompany: {company_id}")
        company = Follow.query.filter_by(
            company_id=company_id, client_id=client_id).first()
        if (company == None):
            new_follow = Follow(
                client_id=client_id,
                company_id=company_id
            )

            new_follow.save()

            return new_follow
        else:
            return None

    @auth_jwt_required
    @marshal_with(
        resource_fields)
    def get(self, current_user):
        follows = Follow.query.filter_by(client_id=int(current_user.id)).all()
        return [{"id": follow.id, "company": marshal(follow.company, resource_fields_follow_company)} for follow in follows]


class CompanyResource(Resource):
    @auth_jwt_required
    @marshal_with(
        resource_fields_follow_company)
    def get(self, current_user):
        args = parser_search_company.parse_args(request)
        search = str("%{}%").format(str(args.get("search", "")))
        return Company.query.filter(Company.company_name.like(
            search)).filter_by(state=current_user.state).all()
