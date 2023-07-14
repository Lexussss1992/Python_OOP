from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            [d for d in self.users if d.driving_license_number == driving_license_number][0]
        except IndexError:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

        return f'{driving_license_number} has already been registered to our platform.'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ('PassengerCar', 'CargoVan'):
            return f'Vehicle type {vehicle_type} is inaccessible.'

        try:
            [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        except IndexError:
            if vehicle_type == 'PassengerCar':
                self.vehicles.append(PassengerCar(brand, model, license_plate_number))
                return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'
            elif vehicle_type == 'CargoVan':
                self.vehicles.append(CargoVan(brand, model, license_plate_number))
                return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

        return f'{license_plate_number} belongs to another vehicle.'

    def allow_route(self, start_point: str, end_point: str, length: float):



app = ManagingApp()

print(app.register_user( 'Tisha', 'Reenie', '7246506' ))

print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))

print(app.register_user( 'Mack', 'Cindi', '7246506'))

print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))

print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))

print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))

print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))

print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))

print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))

print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))