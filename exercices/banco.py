class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.valid = False

    def __repr__(self):
        return f"Usuario {self.valid}"

    def login(self) -> None:
        if self.password == '1234':
            self.valid = True
            print('Iniciar Sesión')
        else:
            print('Usuario o contraseña erroneo')

    @staticmethod
    def disconnect() -> None:
        print('Cerrar sesión')


class Bank:
    def __init__(self):
        self.__users = [
            {'id': 1, 'name': 'Santander', 'amount': 20000, 'pass': '1234', 'username': 'gonza'}
        ]

    def get_users(self):
        return self.__users

    def valid_user(self, user) -> bool:
        print(user)
        userValid = [x for x in self.__users if x["pass"] == user.password]
        print(len(userValid) == 1)
        return len(userValid) == 1


bank = Bank()
gonza = User('Gonzalo', '1234')
gonza.login()
print(gonza)
print(bank.get_users())
bank.valid_user(gonza)
logout = False
while not logout:
    print("\t Banco Santander")
    logout = True if int(input("Ingresa tu respuesta: ")) == 1 else False
