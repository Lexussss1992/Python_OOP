from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_TYPES_OF_BREAD = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }

    VALID_BOOTH_TYPES = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }

    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if type_delicacy not in self.VALID_TYPES_OF_BREAD:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f'{name} already exists!')

        self.delicacies.append(self.VALID_TYPES_OF_BREAD[type_delicacy](name, price))
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f'{type_booth} is not a valid booth!')

        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise f'Booth number {booth_number} already exists!'

        self.booths.append(self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity))
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        booth = next(filter(lambda b: b.is_reserved is False and b.capacity >= number_of_people, self.booths))

        if not booth:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth.reserve(number_of_people)
        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))

        if not booth:
            raise Exception(f'Could not find booth {booth_number}!')

        if not delicacy:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth.delicacy_orders.append(delicacy)
        return f'Booth {booth.booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        total = 0

        for booth in self.booths:
            if booth.booth_number == booth_number:
                for delicacy in booth.delicacy_orders:
                    total += delicacy.price
                total += booth.price_for_reservation
                booth.price_for_reservation = 0
                booth.is_reserved = False
                booth.delicacy_orders = []

        self.income += total
        return f"Booth {booth_number}:\nBill: {total:.2f}lv."

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'