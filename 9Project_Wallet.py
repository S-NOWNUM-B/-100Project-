class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def add_mony(self, new_balance):
        self.balance += new_balance
        return f"Ваш счет был пополнен на сумму {new_balance}$"

    def get_balance(self, new_balance):
        self.balance -= new_balance
        return f"С вашего счёта было снято {new_balance}$"

    def __str__(self):
        return f"Ваш баланс равен {self.balance}$"

wa = Wallet(100)
print(wa)

print(wa.add_mony(150))
print(wa)

print(wa.get_balance(50))
print(wa)