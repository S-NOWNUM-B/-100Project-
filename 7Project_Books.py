class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"У такого писателя как {self.author} есть книга под названием {self.title}. Данная книга насщитывает {self.pages} страниц"

book1 = Book("Автостопом по галактике", "Стас", 342)
book2 = Book("Зима", "Артём", 92)

print(book1)
print(book2)