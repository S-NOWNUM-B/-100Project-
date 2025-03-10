import random

class Generator:
    def __init__(self):
        self.min_dip = None
        self.max_dip = None
        self.znach = None

    def get_range(self):
        while True:
            try:
                self.min_dip = float(input("\nВведите минимальное значение диапазона: ").strip())
                self.max_dip = float(input("Введите максимальное значение диапазона: ").strip())

                if self.min_dip > self.max_dip:
                    print("\nОшибка! Минимальное значение не может быть больше максимального.")
                elif self.min_dip == self.max_dip:
                    print("\nОшибка! Диапазон не может состоять из одного числа.")
                else:
                    break
            except ValueError:
                print("\nОшибка! Введите числовые значения для диапазона.")

    def get_type(self):
        while True:
            self.znach = input("Числа должны быть целыми или дробными? ").strip().lower()
            if self.znach in ("целые", "дробные"):
                break
            else:
                print("\nОшибка! Нужно ввести 'целые' или 'дробные'. Попробуйте снова.\n")

    def generate(self):
        if self.znach == "целые":
            return random.randint(int(self.min_dip), int(self.max_dip))
        elif self.znach == "дробные":
            return random.uniform(self.min_dip, self.max_dip)

def main():
    generator = Generator()

    while True:
        print("\nГенератор случайных чисел")
        print("1. Начать")
        print("2. Выйти")

        choice = input("Выберите действие - ").strip().lower()

        if choice == "начать":
            generator.get_range()
            generator.get_type()
            result = generator.generate()
            print(f"\nВаше случайное число: {result}")

        elif choice == "выйти":
            print("\nКонец работы!")
            break
        else:
            print("\nНеверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
    
