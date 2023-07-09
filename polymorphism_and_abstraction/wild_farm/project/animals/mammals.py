from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if Food.__name__ == 'Vegetable' or Food.__name__ == 'Fruit':
            self.weight += food.quantity * 0.10
        return f'{self.name} does not eat {Food.__name__}!'


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof"

    def feed(self, food: Food):
        if Food.__name__ == 'Meat':
            self.weight += food.quantity * 0.40
        return f'{self.name} does not eat {Food.__name__}!'


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if Food.__name__ == 'Vegetable' or Food.__name__ == 'Meat':
            self.weight += food.quantity * 0.30
        return f'{self.name} does not eat {Food.__name__}!'


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if Food.__name__ == 'Meat':
            self.weight += food.quantity * 1
        return f'{self.name} does not eat {Food.__name__}!'