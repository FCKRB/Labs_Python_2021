from product import Product


class Smartphone(Product):
    def __init__(self, name, price_rub, manufacturer, memory):
        Product.__init__(self, name, price_rub, manufacturer)
        self.__memory = memory

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    def __str__(self):
        return f"Smartphone({self.name}, {self.price_rub}, {self.manufacturer}, {self.memory})"

    def increase_price_rub(self, to_add):
        if "Samsung" in self.manufacturer:
            self.price_euros += to_add
        else:
            self.price_rub += to_add
