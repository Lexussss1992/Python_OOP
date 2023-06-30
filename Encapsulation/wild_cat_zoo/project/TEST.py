from project.animal import Animal
from project.cheetah import Cheetah
from project.lion import Lion
from project.zoo import Zoo

zoo = Zoo("Zootopia", 3000, 5, 8)
c = Cheetah("Cheeto", "Male", 2)
a = Animal("Cheeto", "Male", 2, 100)
print(c.money_for_care)
print(a.money_for_care)