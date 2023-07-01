class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight
        
    @property
    def topping_type(self):
        return self.topping_type

    @topping_type.setter
    def topping_type(self, value):
        if value != '':
            self.topping_type = value
        else:
            return 'The topping type cannot be an empty string'
        
    @property
    def weight(self):
        return 
    
    @weight.setter
    def weight(self, value):
        if value > 0:
            self.weight = value
        else:
            return '"The weight cannot be less or equal to zero"'