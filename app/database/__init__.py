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
        print("Init Create Tables")
        db.create_all()
        print("Finish process of creation tables")

    @server.cli.command()
    def drop_tables():
        '''Drop database'''
        print("Init drop Tables")
        db.drop_all()
        print("Finish process of drop tables")

    @server.cli.command()
    def refresh():
        '''Initialize database'''
        print("Init drop Tables")
        db.drop_all()
        print("Init create Tables")
        db.create_all()
        print("Finish Tables")

    server.cli.add_command(database)
