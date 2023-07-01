from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name,
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        try:
            if value != '':
                self.name = value
        except ValueError:
            return 'The name cannot be an empty string'
        
    @property
    def dough(self):
        return self.dough
    
    @dough.setter
    def dough(self, value):
        try:
            if value is not None:
                self.dough = value
        except ValueError:
            return 'You should add dough to the pizza'
    
    @property
    def max_number_of_toppings(self):
        return self.max_number_of_toppings
    
    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        try:
            if self.max_number_of_toppings > 0:
                self.max_number_of_toppings = value
        except ValueError:
            return 'The maximum number of toppings cannot be less or equal to zero'

    def add_topping(self, topping: Topping):
        try:
            if len(self.toppings) < self.max_number_of_toppings:
                self.toppings[topping.topping_type] = topping.weight
        except ValueError:
            return 'Not enough space for another topping'

    def calculate_total_weight(self):
        total_weight = Dough.weight + Topping.weight
        return total_weight