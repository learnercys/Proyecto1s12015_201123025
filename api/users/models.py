
from general.models import AVLTree


class User:

    def __init__(self):
        self.users = AVLTree()

    def find(self, data):
        return self.users.find(data.get('username'))

    def insert(self, data):
        self.users.insert(
            data.get('username'), {
                'name': data.get('name'),
                'address': data.get('address'),
                'password': data.get('password'),
                'phoneNumber': data.get('phoneNumber'),
                'creditCardNumber': data.get('creditCardNumber'),
                'actualAddress': data.get('actualAddress')
            }
        )

    def get_users(self):
        return self.users.inorder()


class Auth:
    def __init__(self):
        self.__load_all()

    def __load_all(self):
        import os
        import json
        self.sessions = json.load(open(os.path.join(os.path.dirname(__file__), "../database.json")))['sessions']

