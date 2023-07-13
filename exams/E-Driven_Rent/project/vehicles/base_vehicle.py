class BaseVehicle:
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level: int = 100
        self.is_damaged: bool = False

    @property
    def brand(self):
        if self._brand == '' or self._brand.isspace():
            raise ValueError('Brand cannot be empty!')
        else:
            return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        if self._model == '' or self._model.isspace():
            raise ValueError('Model cannot be empty!')
        else:
            return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def license_plate_number(self):
        if self._license_plate_number == '' or self._license_plate_number.isspace():
            raise ValueError('License plate number is required!')
        else:
            return self._license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        self._license_plate_number = value

    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        if self.is_damaged is True:
            self.is_damaged = False
        else:
            self.is_damaged = True

    def __str__(self):
        if self.is_damaged is True:
            return f'{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: Damaged'
        return f'{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: OK'