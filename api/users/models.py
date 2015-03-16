from overload import overload
from general.models import AVLTree


class User:

    def __init__(self):
        self.users = AVLTree()


class Auth:
    def __init__(self):
        self.__load_all()

    def __load_all(self):
        import os
        import json
        self.sessions = json.load(open(os.path.join(os.path.dirname(__file__), "../database.json")))['sessions']

