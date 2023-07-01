from project.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.grams = grams

    @property
    def attribute_grams(self):
        return self.grams