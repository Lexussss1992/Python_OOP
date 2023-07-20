from abc import ABC, abstractmethod
from typing import List


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: List[object] = []

    @property
    def name(self):
        if self._name == '' or self._name.isspace():
            raise ValueError('Service name cannot be empty!')
        else:
            return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def capacity(self):
        if self._capacity <= 0:
            raise ValueError('Service capacity cannot be less than or equal to 0!')
        else:
            return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @staticmethod
    @abstractmethod
    def details():
        pass