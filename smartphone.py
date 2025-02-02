class Smartphone:
    # Конструктор класса принимает марку, модель и номер телефона
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    # Метод для красивого вывода информации о смартфоне
    def get_info(self):
        return f"{self.brand} - {self.model}. {self.phone_number}"