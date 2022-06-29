from pydoc import cli
from flask import Flask
from flask.cli import AppGroup
from app.extensions import db
from .actions import shell_context
from ..models.client import Client


def init_app(server: Flask):
    database = AppGroup('database', help='Help user with database (ORM).')

    @server.shell_context_processor
    def make_shell_context():
        return shell_context(server, db, Client)

    @server.cli.command()
    def create_tables():
        '''Initialize database'''
        db.create_all()

    @server.cli.command()
    def drop_tables():
        '''Initialize database'''
        db.create_all()

    @server.cli.command()
    def refresh():
        '''Initialize database'''
        db.drop_all()
        db.create_all()

    server.cli.add_command(database)
