from abc import ABC, abstractmethod


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight


    @property
    def name(self):
        if self._name == '' or self._name.isspace():
            raise ValueError('Robot name cannot be empty!')
        else:
            return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def kind(self):
        if self._kind == '' or self._kind.isspace():
            raise ValueError('Robot kind cannot be empty!')
        else:
            return self._kind
    
    @kind.setter
    def kind(self, value):
        self._kind = value

    @property
    def price(self):
         if self._price <= 0:
             raise ValueError('Robot price cannot be less than or equal to 0.0!')

    @price.setter
    def price(self, value):
        self._price = value

    @staticmethod
    @abstractmethod
    def eating():
        pass