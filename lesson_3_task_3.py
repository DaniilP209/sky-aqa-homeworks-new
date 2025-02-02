from address import Address
from mailing import Mailing

# Создаем объекты адресов
to_address = Address("123456", "Москва", "Ленина", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "30")

# Создаем объект почтового отправления
mail = Mailing(to_address, from_address, 350, "AB123456789RU")

# Выводим информацию о почтовом отправлении
print(mail.get_info())