from overload import overload


class User:

    def __init__(self):
        self.root = None
        self.__load_all()

    def get_all(self):
        return self.users

    @overload
    def append(self, user):
        self.append(user, self.root)

    @append.add
    def append(self, user, node):
        if node is None:
            node.username = user.username
            # append the user to the current node
        else:
            if user.username < node.username:
                self.append(user, node.left)
            else:
                self.append(user, node.rigth)

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

    class Node:
        def __init__(self, username):
            # the order in the users tree
            self.username = username