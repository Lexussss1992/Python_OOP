class GFG:
    def __init__(self, val):
        self.val = val

    def __add__(self, val2):
        return GFG(self.val + val2.val)


obj1 = GFG("Geeks")
obj2 = GFG("ForGeeks")
obj3 = obj1 + obj2
print(obj3.val)