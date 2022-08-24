from flask_restful import Api
from . import client, company, auth


def init_router(api: Api):

    api.add_resource(client.ClientResource, "/clients",
                     "/clients/<int:client_id>")
    api.add_resource(company.CompanyResource, "/companies",
                     "/companies/<int:company_id>")
    api.add_resource(auth.Login, "/auth")
    return api
