from abc import ABC, abstractmethod
from typing import List


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: List[object] = []

    @property
    def name(self):
        if self.__name == '' or self.__name.isspace():
            raise ValueError('Service name cannot be empty!')
        else:
            return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def capacity(self):
        if self.__capacity <= 0:
            raise ValueError('Service capacity cannot be less than or equal to 0!')

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @staticmethod
    @abstractmethod
    def details():
        pass