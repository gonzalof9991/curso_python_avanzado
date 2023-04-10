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

