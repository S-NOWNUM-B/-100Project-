class Bank:
    def __init__(self, balance, plus_mony, minus_mony):
        self.balance = balance
        self._plus_mony = plus_mony
        self._minus_mony = minus_mony

    def __str__(self):
        return f"Ваш баланс: {self.balance}$"

class Action(Bank):
    def __init__(self, balance, plus_mony, minus_mony):
        super().__init__(balance, plus_mony, minus_mony)

    @property
    def plus_mony(self):
        return self._plus_mony

    @plus_mony.setter
    def plus_mony(self, money):
        self._plus_mony += money
        self.balance += money
        print(f"Вы пополнили свой баланс на {money}$. Новый баланс: {self.balance}$")

    @property
    def minus_mony(self):
        return self._minus_mony

    @minus_mony.setter
    def minus_mony(self, money):
        if self.balance >= money:
            self._minus_mony += money
            self.balance -= money  # Уменьшаем баланс
            print(f"Со своего счёта вы сняли {money}$. Новый баланс: {self.balance}$")
        else:
            print("Ошибка! Недостаточно средств на счёте.")

    def __str__(self):
        return f"Ваш баланс: {self.balance}$"

b = Action(100, 250, 50)

b.plus_mony = 500
b.minus_mony = 375

print(b)