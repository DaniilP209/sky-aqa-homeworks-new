class User:
    # Конструктор принимает имя и фамилию
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Метод для вывода имени
    def print_first_name(self):
        print("Имя:", self.first_name)

    # Метод для вывода фамилии
    def print_last_name(self):
        print("Фамилия:", self.last_name)

    # Метод для вывода имени и фамилии вместе
    def print_full_name(self):
        print("Полное имя:", self.first_name, self.last_name)