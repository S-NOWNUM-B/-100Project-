class Calculator:
    def __init__(self, number1, number2, action):
        self.number1 = number1
        self.number2 = number2
        self.action = action

    def calculate(self):
        if self.action == "+":
            return f"{self.number1} + {self.number2} = {self.number1 + self.number2}"
        elif self.action == "-":
            return f"{self.number1} - {self.number2} = {self.number1 - self.number2}"
        elif self.action == "*":
            return f"{self.number1} * {self.number2} = {self.number1 * self.number2}"
        elif self.action == "/":
            if self.number2 == 0:
                return "ОШИБКА: делить на 0 нельзя"
            else:
                return f"{self.number1} / {self.number2} = {self.number1 / self.number2}"

cal1 = Calculator(7, 2, "+")
cal2 = Calculator(1, 3, "-")
cal3 = Calculator(8, 11, "*")
cal4 = Calculator(15, 5, "/")
cal5 = Calculator(15, 0, "/")

print(cal1.calculate())
print(cal2.calculate())
print(cal3.calculate())
print(cal4.calculate())
print(cal5.calculate())