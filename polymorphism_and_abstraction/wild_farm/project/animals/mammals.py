from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Vegetable' or food.__class__.__name__ == 'Fruit':
            self.weight += food.quantity * 0.10
            self.food_eaten += food.quantity
        return f'{self.name} does not eat {food.__class__.__name__}!'


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 0.40
            self.food_eaten += food.quantity
        return f'{self.name} does not eat {food.__class__.__name__}!'


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Vegetable' or food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 0.30
            self.food_eaten += food.quantity
        return f'{self.name} does not eat {food.__class__.__name__}!'


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 1
            self.food_eaten += food.quantity
        return f'{self.name} does not eat {food.__class__.__name__}!'