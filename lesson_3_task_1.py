from user import User

# Создаем экземпляр класса User
my_user = User("Иван", "Петров")

# Вызываем методы объекта my_user
my_user.print_first_name()  # Выведет: Имя: Иван
my_user.print_last_name()   # Выведет: Фамилия: Петров
my_user.print_full_name()   # Выведет: Полное имя: Иван Петров