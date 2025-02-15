class Phone:
    def __init__(self, manufacturer, model, battery):
        self.manufacturer = manufacturer
        self.model = model
        self.battery = battery

    def get_phone(self, new_manufacturer, new_model, new_battery):
        self.manufacturer = new_manufacturer
        self.model = new_model
        self.battery = new_battery
        return f"Новый телефон вы хотите от {self.manufacturer}, модель {self.model}. Данный телефон должен иметь {self.battery} mAh заряда батареи"

    def __str__(self):
        return f"У вас сейчас {self.manufacturer}, модель {self.model}. Имеет {self.battery} mAh заряда батареи"

ph = Phone("Iphone", "14 Pro Max", 5000)
print(ph)

print(ph.get_phone("SUMSUNG", "S 25 Ultra", 8000))
print(ph)