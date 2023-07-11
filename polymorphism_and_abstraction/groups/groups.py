class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, surname):
        return Person(self.name, surname.surname)


# class GFG:
#     def __init__(self, val):
#         self.val = val
#
#     def __add__(self, val2):
#         return GFG(self.val + val2.val)


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
print(p4)

