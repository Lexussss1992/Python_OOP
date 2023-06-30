from typing import List

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal, price):
        new_budget = self.__budget - price
        if len(self.animals) < self.__animal_capacity and new_budget > 0:
            self.__budget -= price
            self.animals.append(animal)
            return f"{self.name} the {animal} added to the zoo"

        if len(self.animals) < self.__animal_capacity and new_budget <= 0:
            return "Not enough budget"

        return "Not enough space for animal"

    # def hire_worker(self, worker):
    #
