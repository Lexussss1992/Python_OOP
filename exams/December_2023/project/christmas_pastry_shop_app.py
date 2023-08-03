from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy


class ChristmasPastryShopApp:
    VALID_TYPES_OF_BREAD = [
        'Gingerbread',
        'Stolen'
    ]

    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        delicacy = next(filter(lambda d: d.name == name, self.delicacies))

        if delicacy:
            raise Exception(f'{name} already exists!')

        if type_delicacy not in self.VALID_TYPES_OF_BREAD:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        self.delicacies.append(delicacy)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'