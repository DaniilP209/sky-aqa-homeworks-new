from smartphone import Smartphone

# Создаем список catalog
catalog = []

# Добавляем 5 экземпляров класса Smartphone в список
catalog.append(Smartphone("Apple", "iPhone 14", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 7", "+79456789012"))
catalog.append(Smartphone("OnePlus", "10 Pro", "+79567890123"))

# Перебираем список и выводим информацию о каждом смартфоне
for phone in catalog:
    print(phone.get_info())