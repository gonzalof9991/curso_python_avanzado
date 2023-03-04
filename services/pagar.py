from typing import *
class Payment:
    # Siempre debe ir self, para inicializar el objeto en Python

    pin_pass = '1234'
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"Tarjeta {self.name}, {self.amount}."

    def __repr__(self):
        return f"<Tarjeta({self.name}, {self.amount})>"

    def payment(self, amount: int):
        self.amount -= amount
        print(self.pin_pass)



tarjetaSantander = Payment("Santander", "Debito", 150000)
tarjetaSantander.payment(400)
print(tarjetaSantander)