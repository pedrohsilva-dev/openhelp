from flask import Flask
from app.website.views.router import router


def init_app(server: Flask):
    """init and register routes webpages"""
    return router.register(server)
