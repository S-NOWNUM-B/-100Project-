class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} - {self.price}$"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_cost(self):
        total = sum(product.price for product in self.products)
        return total

product1 = Product("Молоко", 50)
product2 = Product("Хлеб", 30)
product3 = Product("Сыр", 100)

store = Store()
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

print("Товары в магазине:")
for product in store.products:
    print(product)

print(f"Общая стоимость покупок: {store.total_cost()}$")
