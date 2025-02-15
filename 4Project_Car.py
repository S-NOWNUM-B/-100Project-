class Car:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed
        self.new_make = ""
        self.new_model = ""
        self.new_speed = ""

    def New_Car(self):
        self.new_make = input("Введите марку машины, которую вы бы хотели - ")
        self.new_model = input("Введите модель машины, которую вы бы хотели - ")
        self.new_speed = input("Введите максимальную скорость, до которой хотели бы разогнаться - ")

    def __str__(self):
        return f"Ваша текущая машина: {self.make} {self.model} с максимальной скоростью {self.speed} км/ч\nВы хотите машину: {self.new_make} {self.new_model} с максимальной скоростью {self.new_speed} км/ч"

car = Car(input("Введите марку машины, которая у вас есть - "),
          input("Введите модель машины, которая у вас есть - "),
          input("Введите максимальную скорость, которую вы достигли на этой машине - "))

car.New_Car()

print(car)