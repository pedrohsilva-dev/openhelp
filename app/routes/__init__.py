from flask_restful import Api
from . import user


def init_router(api: Api):

    api.add_resource(user.ClientResource, "/clients")

    return api
