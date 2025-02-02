class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    # Метод для красивого отображения адреса
    def get_address(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house} - {self.apartment}"