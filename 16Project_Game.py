from datetime import *
import time
import random

class Game:

    def __init__(self, title):
        self.title = title

    def countdown(self):
        start = datetime.now()
        end = start + timedelta(seconds=4)

        while datetime.now() < end:
            remaining = (end - datetime.now()).seconds
            print(f"\rКамень! Ножницы! Бумага! {remaining}", end="", flush=True)
            time.sleep(1)

    def __str__(self):
        return f"Вы выбрали {self.title}"

class Action(Game):
    words = ["Камень", "Ножницы", "Бумага"]

    def __init__(self, title):
        super().__init__(title)

    def game(self):
        random_word = random.choice(self.words)
        print(f"\nКомпьютер выбрал - {random_word}")

        if self.title == random_word:
            print("Ничья!")
        elif (self.title == "Камень" and random_word == "Ножницы") or \
                (self.title == "Ножницы" and random_word == "Бумага") or \
                (self.title == "Бумага" and random_word == "Камень"):
            print("Вы победили!")
        else:
            print("Вы проиграли!")

player_choice = input("Введите 'Камень', 'Ножницы' или 'Бумага' - ").capitalize()

if player_choice in Action.words:
    game = Action(player_choice)
    print(game)
    game.countdown()
    game.game()
else:
    print("Некорректный выбор. Попробуйте снова.")