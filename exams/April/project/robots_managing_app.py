from typing import List

from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        'MainService': MainService,
        'SecondaryService': SecondaryService
    }

    VALID_ROBOT_TYPES = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot
    }

    def __init__(self):
        self.robots: List[object] = []
        self.services: List[object] = []

    def add_service(self, service_type: str, name: str):

        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception('Invalid service type!')

        service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)

        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception('Invalid robot type!')

        robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)

        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        robot = [r for r in self.robots if r.name == robot_name][0]

        if service.capacity <= len(self.robots):
            raise Exception('Not enough capacity for this robot!')

        if not ((robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'MainService') or (robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'SecondaryService')):
            return 'Unsuitable service.'

        self.robots.remove(robot)
        service.robots.append(robot)
        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.services if r.name == robot_name][0]

        if not robot:
            return 'No such robot in this service!'

        self.services.remove(robot)
        self.robots.append(robot)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        [r.eating() for r in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = sum([r.price for r in service.robots])

        return f'The value of service {service_name} is {total_price}.'

    def __str__(self):
        for s in self.services:
            res = []
            res.append(s)
        return '\n'.join(i.details() for i in res)

main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))
print(str(main_app))