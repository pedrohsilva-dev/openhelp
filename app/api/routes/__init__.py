from flask import Flask, make_response
from flask_restful import Api
from app.api.routes import client, company, auth, warnings


def init_router(api: Api, server: Flask):

    api.add_resource(client.ClientResource, "/clients",
                     "/clients/<int:client_id>")
    api.add_resource(company.FollowResource, "/follows",
                     "/follows/<int:client_id>")
    api.add_resource(auth.Login, "/auth")
    api.add_resource(warnings.WarningResource, "/warnings")
    api.add_resource(company.CompanyResource, "/companies")

    api.init_app(server)

    return server
