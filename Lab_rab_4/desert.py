from food import Food


class Desert(Food):
    def __init__(self, name, price_rub, manufacturer, nutrition, sugar):
        super().__init__(name, price_rub, manufacturer, nutrition + 3*sugar)
        self.__sugar = sugar

    @property
    def sugar(self):
        return self.__sugar

    @sugar.setter
    def sugar(self, categories):
        self.__sugar = categories

    def __str__(self):
        return f"Desert({self.name}, {self.price_rub}, {self.manufacturer}, {self.nutrition}, {self.sugar})"
