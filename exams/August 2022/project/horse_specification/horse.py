from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name: str = name
        self.speed: int = speed
        self.is_taken: bool = False

    @staticmethod
    def check_speed(name, speed):
        if speed > 120 and name == 'Appaloosa':
            raise ValueError('Horse speed is too high!')
        elif speed > 140 and name == 'Thoroughbred':
            raise ValueError('Horse speed is too high!')
        else:
            return speed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = self.check_speed(self.name, value)

    @staticmethod
    @abstractmethod
    def train(self):
        pass
