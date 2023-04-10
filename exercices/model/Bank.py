
class Bank:
    def __init__(self):
        self.__users = [
            {'id': 1, 'name': 'Santander', 'amount': 20000, 'pass': '1234', 'username': 'gonza'}
        ]

    def get_users(self):
        return self.__users

    def add_user(self, user):
        new_user = {'id': 1, 'name': 'Santander', 'amount': 20000, 'pass': '1234', 'username': 'Luis'}
        self.__users.append(new_user)
        print(len(self.__users))

    def valid_user(self, user) -> bool:
        print(user)
        userValid = [x for x in self.__users if x["pass"] == user.password]
        print(len(userValid) == 1)
        return len(userValid) == 1
