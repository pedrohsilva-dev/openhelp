# libs that it is system core

import os
from flask import Flask
from flask_restful import Api


from app.system import database, extensions
from app.system.services import authentication
from app.api import routes
from app.website import views


def create_app(config=None):
    """
        :param: config configuration archive config.py
        :description: Factory that make initial app
        of the Server
    """

    server = Flask(__name__)

    # Init Configuration
    server.config.from_object(config())

    # Init Extensions
    extensions.init_app(server)

    # Init Commands Shell
    database.init_app(server)

    # init authentication
    authentication.init_app(server)

    # Init api
    api = Api(
        prefix=os.environ.get("PREFIX_URL")
        if os.environ.get("PREFIX_URL") != None
        else "/api"
    )
    # put /api init of the URL

    # Init APP(API RESTful)
    routes.init_router(
        api             # init routes of API
    ).init_app(server)

    # Start WebApplication
    views.init_app(server)

    # return instance Flask
    return server
