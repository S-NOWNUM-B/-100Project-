import calendar
import pickle

FILE_NAME = "tasks.pkl"

def load_tasks():
    try:
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

def save_tasks(tasks):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(tasks, file)

class CalendarApp:
    def __init__(self):
        self.tasks = load_tasks()

    def show_calendar(self, year, month):
        print(calendar.month(year, month))

    def add_task(self, year, month, day, task):
        date_key = f"{year}-{month:02d}-{day:02d}"

        if date_key in self.tasks:
            self.tasks[date_key].append(task)
        else:
            self.tasks[date_key] = [task]
        save_tasks(self.tasks)
        print(f"Дело добавлено на {date_key}: {task}")

    def show_tasks(self, year, month, day):
        date_key = f"{year}-{month:02d}-{day:02d}"

        if date_key in self.tasks:
            print(f"\nДела на {date_key}:")
            for idx, task in enumerate(self.tasks[date_key], 1):
                print(f"{idx}. {task}")
        else:
            print(f"\nНа {date_key} дел нет")

    def show_all_tasks(self):
        if not self.tasks:
            print("\nНет задач в календаре.")
        else:
            print("\nВсе задачи:")
            for date_key, task_list in self.tasks.items():
                print(f"\n{date_key}:")
                for idx, task in enumerate(task_list, 1):
                    print(f"  {idx}. {task}")

def main():
    app = CalendarApp()
    while True:
        print("\nКалендарь с делами")
        print("1. Показать календарь")
        print("2. Добавить дело")
        print("3. Просмотреть дела")
        print("4. Просмотреть все дела")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            year = int(input("Введите год: "))
            month = int(input("Введите месяц (1-12): "))
            app.show_calendar(year, month)

        elif choice == "2":
            year = int(input("Введите год: "))
            month = int(input("Введите месяц (1-12): "))
            day = int(input("Введите день: "))
            task = input("Введите дело: ")
            app.add_task(year, month, day, task)

        elif choice == "3":
            year = int(input("Введите год: "))
            month = int(input("Введите месяц (1-12): "))
            day = int(input("Введите день: "))
            app.show_tasks(year, month, day)

        elif choice == "4":
            app.show_all_tasks()

        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()