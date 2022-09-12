from types import FunctionType
from typing import List
from flask import Flask


class Route:
    def __init__(self, name: str, action: FunctionType, methods: List[str], endpoint: str = None):
        self.__name = name
        self.__action = action
        self.__methods = methods
        self.__endpoint = endpoint

    @property
    def name(self):
        return self.__name

    @property
    def action(self):
        return self.__action

    @property
    def methods(self):
        return self.__methods

    @property
    def endpoint(self):
        return self.__endpoint


class Router:
    __routes: List[Route] = []

    def add(self, route: Route):
        self.__routes.append(route)

    def register(self, server: Flask):
        for route in self.__routes:
            controller = route.action
            controller.methods = route.methods
            controller.provide_automtic_options = False
            # print(f"Route: {route.name}")
            # print("Methods:")
            # for i in controller.methods:
            #     print(f"\t{i}")
            # print("-------------------------------------------")
            server.add_url_rule(
                rule=route.name,
                view_func=controller,
                endpoint=route.endpoint
            )

        return server
