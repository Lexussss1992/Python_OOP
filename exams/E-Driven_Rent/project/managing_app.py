from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

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
        try:
            route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point][0]
            if route.length == length:
                return f'{start_point}/{end_point} - {length} km had already been added to our platform.'
            elif route.length < length:
                return f'{start_point}/{end_point} shorter route had already been added to our platform.'
            elif route.length > length:
                route.is_locked = True
                self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
                return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'
        except IndexError:
            self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
            return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f'User {driving_license_number} is blocked in the platform! This trip is not allowed.'

        if vehicle.is_damaged:
            return f'Vehicle {license_plate_number} is damaged! This trip is not allowed.'

        if route.is_locked:
            return f'Route {route_id} is locked! This trip is not allowed.'

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        if vehicle.is_damaged:
            return f'{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: Damaged'
        else:
            return f'{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: OK'

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged is True]
        damaged_vehicles_sorted = sorted(damaged_vehicles, key=lambda x: x.model)

        if len(damaged_vehicles) == 0:
            return f'{len(damaged_vehicles_sorted)} vehicles were successfully repaired!'

        for v in range(len(damaged_vehicles_sorted)):
            if v <= count:
                damaged_vehicles_sorted[v].is_damaged = False
                damaged_vehicles_sorted[v].battery_level = 100
            return f'{len(damaged_vehicles_sorted)} vehicles were successfully repaired!'

    def users_report(self):
        users = [u for u in self.users]
        sorted_users = sorted(users, key=lambda x: x.rating, reverse=True)
        new_line = '\n'

        return f'*** E-Drive-Rent ***\n' \
               f'{f"{new_line}".join([u.__str__() for u in sorted_users])}'