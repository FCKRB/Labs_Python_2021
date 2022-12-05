from product import Product


class Food(Product):
    def __init__(self, name, price_rub, manufacturer, nutrition):
        super().__init__(name, price_rub, manufacturer)
        self.__nutrition = nutrition

    @property
    def nutrition(self):
        return self.__nutrition

    @nutrition.setter
    def nutrition(self, nutrition):
        self.__nutrition = nutrition

    def __str__(self):
        return f"Food({self.name}, {self.price_rub}, {self.manufacturer}, {self.nutrition})"
