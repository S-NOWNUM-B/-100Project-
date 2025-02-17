class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __str__(self):
        return f"Вашу {self.species} зовут {self.name}, возрастом {self.age} лет"

class Action(Pet):
    def __init__(self, name, age, species, game=False, food=False):
        super().__init__(name, age, species)
        self.game = game
        self.food = food

    def add_food(self):
        if not self.food:
            otv = input(f"Вашу {self.species} нужно покормить. Вы это хотите сделать? [да/нет] ").lower().strip()
            if otv == "да":
                self.food = True
                return f"Вы накормили {self.name}"
            else:
                return f"Вы решили не кормить {self.name}"
        return f"Ваша {self.species} уже накормлена"

    def add_game(self):
        if not self.game:
            otv = input(f"Вы хотите поиграть с {self.name}? [да/нет] ").lower().strip()
            if otv == "да":
                self.game = True
                return f"Вы поиграли с {self.name}. Теперь {self.name} счастлив!"
            else:
                return f"Вы решили не играть с {self.name}"
        return f"С вашей {self.species} уже поиграли"

    def __str__(self):
        return f"{self.species} по имени {self.name} возрастом {self.age} лет, его накормили? {self.food}. С ним поиграли? {self.game}"

# Создаём объекты
p1 = Pet("Рекс", 10, "собака")
p2 = Pet("Багира", 8, "кошка")
p3 = Pet("Шарик", 3, "птица")
print(p1)
print(p2)
print(p3)

p1 = Action("Рекс", 10, "собака", game=False, food=False)
p2 = Action("Багира", 8, "кошка", game=True, food=True)
p3 = Action("Шарик", 3, "птица", game=False, food=True)

print(p1.add_game())
print(p1.add_food())

print(p2.add_food())

print(p3.add_game())

print(p1)
print(p2)
print(p3)