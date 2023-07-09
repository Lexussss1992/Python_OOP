from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ == 'Meat':
            self.weight += food.quantity * 0.25
            self.food_eaten += food.quantity
        return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity
