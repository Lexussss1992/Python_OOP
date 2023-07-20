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

        self.services.append(robot)
        return f'Successfully added {robot_name} to {service_name}.'


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))
print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))