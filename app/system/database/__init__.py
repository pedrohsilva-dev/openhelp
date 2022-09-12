from pydoc import cli
from flask import Flask
from flask.cli import AppGroup
from app.system.extensions import db
from ..models.company import Company
from .actions import shell_context
from ..models.client import Client


def init_app(server: Flask):
    database = AppGroup('database', help='Help user with database (ORM).')

    @server.shell_context_processor
    def make_shell_context():
        return shell_context(server, db, Client, Company)

    @database.command()
    def create_tables():
        '''Initialize database'''
        print("Init Create Tables")
        db.create_all()
        print("Finish process of creation tables")

    @database.command()
    def drop_tables():
        '''Drop database'''
        print("Init drop Tables")
        db.drop_all()
        print("Finish process of drop tables")

    @database.command()
    def seed_tables():
        """ Preenche banco de dados com dados fake """
        for i in range(1, 180):
            db.session.add(Company(
                f"user{i}",
                f"user{i}@gmail.com",
                f"user{i}_1234",
                f"Cidade do user{i}",
                f"SP",
                f"wdosfhidspjfsdj.jpg"
            ))
        db.session.commit()
        db.session.close_all()

    @database.command()
    def refresh():
        '''Initialize database'''
        print("Init drop Tables")
        db.drop_all()
        print("Init create Tables")
        db.create_all()
        print("Finish Tables")

    server.cli.add_command(database)
