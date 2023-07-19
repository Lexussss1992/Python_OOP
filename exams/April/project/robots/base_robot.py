from abc import ABC, abstractmethod


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight


    @property
    def name(self):
        if self.__name == '' or self.__name.isspace():
            raise ValueError('Robot name cannot be empty!')
        else:
            return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def kind(self):
        if self.__kind == '' or self.__kind.isspace():
            raise ValueError('Robot kind cannot be empty!')
        else:
            return self.__kind
    
    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def price(self):
         if self.__price <= 0:
             raise ValueError('Robot price cannot be less than or equal to 0.0!')

    @price.setter
    def price(self, value):
        self.__price = value

    @staticmethod
    @abstractmethod
    def eating():
        pass