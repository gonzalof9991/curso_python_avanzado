from model.User import User
from model.Bank import Bank

bank = Bank()
gonza = User('Gonzalo', '1234')
luis = User('Luis', '1234')
gonza.login()
bank.add_user(luis)
print(gonza)
print(bank.get_users())
# bank.valid_user(gonza)
