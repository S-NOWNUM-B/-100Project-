class Student():
    def __init__(self, number1, number2, number3, number4, number5):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
        self.number4 = number4
        self.number5 = number5

    def calculate(self):
        sr = (self.number1 + self.number2 + self.number3 + self.number4 + self.number5) / 5
        return f"Ваша средняя оценка равна {sr}"

st = Student(5, 5, 3, 4,5)

print(st.calculate())