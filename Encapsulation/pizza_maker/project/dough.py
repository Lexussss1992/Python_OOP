class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.flour_type

    @flour_type.setter
    def flour_type(self, value):
        try:
            if value != '':
                self.flour_type = value
        except ValueError:
            return 'The flour_type type cannot be an empty string'
        
    @property
    def baking_technique(self):
        return 
    
    @baking_technique.setter
    def baking_technique(self, value):
        try:
            if value != '':
                self.baking_technique = value
        except ValueError:
            return 'The baking technique cannot be an empty string'
        
    @property
    def weight(self):
        return 
    
    @weight.setter
    def weight(self, value):
        try:
            if value > 0:
                self.weight = value
        except ValueError:
            return 'The weight cannot be less or equal to zero'