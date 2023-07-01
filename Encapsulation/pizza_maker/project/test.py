from project.dough import Dough
from project.pizza import Pizza

d = Dough("Sugar", "Mixing", 20)
p = Pizza("Burger", d, 5)

print(d.flour_type)
print(p.name)