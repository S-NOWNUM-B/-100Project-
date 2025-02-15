class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self, new_age):
        self.age = new_age
        return f"Ваш новый возраст - {self.age}"

    def __str__(self):
        return f"Привет {self.name}! Я знаю что тебе {self.age}"

hum1 = Human("Стас", 19)
hum2 = Human("Максим", 20)
hum3 = Human("Света", 21)

print(hum1)
print(hum2)
print(hum3)

print(f"\n{hum1.get_age(20)}")

print(f"\n{hum1}")