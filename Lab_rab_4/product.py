class Product:
    def __init__(self):
        self.__name = "No title"
        self.__price_rub = 0
        self.__manufacturer = "No title"

    def __init__(self, name, price_rub, manufacturer):
        self.__name = name
        self.__price_rub = price_rub
        self.__manufacturer = manufacturer

    def __del__(self):
        print(f"{self.name} удален из памяти")

    def __str__(self):
        return f"Product({self.name}, {self.price_rub}, {self.manufacturer})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price_rub(self):
        return self.__price_rub

    @price_rub.setter
    def price_rub(self, price_rub):
        self.__price_rub = price_rub

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def price_euros(self):
        return round(self.__price_rub / 61.05, 4)

    @price_euros.setter
    def price_euros(self, price_euros):
        self.__price_rub =  round(float(price_euros * 61.05), 4)

    def print_with_euros(self):
        print(f"Product({self.name}, {self.price_euros}, {self.manufacturer})")

    def increase_price_rub(self, to_add):
        self.price_rub += to_add
