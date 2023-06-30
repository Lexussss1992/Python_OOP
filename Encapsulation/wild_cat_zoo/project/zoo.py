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
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if len(self.animals) < self.__animal_capacity and new_budget <= 0:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__worker_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):

        result = next(
            (obj for obj in self.workers if obj.name == worker_name),
            None
        )

        if worker_name == result.name:

            self.workers.remove(result)
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        ls_salaries = [i.salary for i in self.workers]
        sum_salaries = sum(ls_salaries)

        if sum_salaries <= self.__budget:
            self.__budget -= sum_salaries

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        ls_money_for_care = [i.money_for_care for i in self.animals]
        sum_money_for_care = sum(ls_money_for_care)

        if sum_money_for_care <= self.__budget:
            self.__budget -= sum_money_for_care

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        nl = '\n'
        lions = [l for l in self.animals if l.__class__.__name__ == 'Lion']
        cheetahs = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']
        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']

        return f"You have {len(self.animals)} animals \n" \
               f"----- {len(lions)} Lions:\n" \
               f"{f'{nl}'.join(i.__repr__() for i in lions)}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{f'{nl}'.join(i.__repr__() for i in tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{f'{nl}'.join(i.__repr__() for i in cheetahs)}\n"

    def workers_status(self):
        nl = '\n'
        keepers = [l for l in self.workers if l.__class__.__name__ == 'Keeper']
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        vets = [t for t in self.workers if t.__class__.__name__ == 'Vet']

        return f"You have {len(self.workers)} workers \n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{f'{nl}'.join(i.__repr__() for i in keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{f'{nl}'.join(i.__repr__() for i in caretakers)}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{f'{nl}'.join(i.__repr__() for i in vets)}\n"



