class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = 0
        # self.is_blocked = False

    @property
    def first_name(self):
        if self._first_name == '' or self._first_name.isspace():
            raise ValueError('First name cannot be empty!')
        else:
            return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        if self._last_name == '' or self._last_name.isspace():
            raise ValueError('Last name cannot be empty!')
        else:
            return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def driving_license_number(self):
        if self._driving_license_number == '' or self._driving_license_number.isspace():
            raise ValueError('Driving license number is required!')
        else:
            return self._driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        self._driving_license_number = value

    @property
    def rating(self):
        if self._rating < 0:
            raise ValueError('Users rating cannot be negative!')
        else:
            return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

# driving_license_number: str, rating: float?


a = User('Ivo', 'gsdf', 'dsadasdad')
print(a.last_name)
print(a.driving_license_number)
print(a.rating)