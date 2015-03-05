from overload import overload


class User:

    def __init__(self):
        self.root = None
        self.__load_all()

    def get_all(self):
        return self.users

    @overload
    def append(self, user):
        if self.root is None:
            self.root = self.Node(user)
            return True
        else:
            return self.append(user, self.root)

    @append.add
    def append(self, user, node):
        if user.username == node.get_username():
            return False    # cannot append the user, already exist.

        elif user.username < node.get_username():
            if node.left is None:
                node.left = self.Node(user)
                return True
            else:
                return self.append(user, node.left)

        else:
            if node.right is None:
                node.right = self.Node(user)
                return True
            else:
                return self.append(user, node.right)

    @overload
    def is_user(self, user):
        return self.is_user(user, self.root)

    @is_user.add
    def is_user(self, user, node):
        if node is None:
            return False

        return self.is_user(user, node.left) if user.username < node.username else self.is_user(user, node.right)

    def search(self, user):
        print(user)
        return 'hello ' + user

    def __load_all(self):
        import os
        import json

        # load the main database
        # I hate cannot use the 'database.users' sentence.
        users_database = json.load(open(os.path.join(os.path.dirname(__file__), "../database.json")))['users']
        self.users = users_database

    class Node:

        """
        :param user { dict } suggested structure:
            {
                'username': '[a-z][a-z0-9]*',
                'name': '',
                'password': '',
                'address': '',
                'phone_number': '',
                'credit_card_number': '',   # encrypted? no.
                'actual_address': ''        # I have no idea why?
            }
        """
        def __init__(self, user):
            # the order in the users tree
            self.__user = user
            self.left = None
            self.right = None

        def get_username(self):
            return self.__user['username']

        def get_name(self):
            return self.__user['name']

        def get_password(self):
            return self.__user['password']  # this is so wrong


class Auth:
    def __init__(self):
        self.__load_all()

    def __load_all(self):
        import os
        import json
        self.sessions = json.load(open(os.path.join(os.path.dirname(__file__), "../database.json")))['sessions']