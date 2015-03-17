
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


import string
import random


class Auth:
    def __init__(self):
        self.tokens = {}

    def save_token(self, username):
        while True:
            _token = self.token_generator()
            if self.tokens.get(_token) is None:
                self.tokens[_token] = username
                return _token

    @staticmethod
    def token_generator(size=40, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


