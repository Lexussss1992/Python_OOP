from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, capacity=30)

    def details(self):

        if len(self.robots) > 0:
            return f"{self.name} Main Service:\n" \
                   f"Robots: {' '.join(r.name for r in self.robots)}"
        else:
            return f"{self.name} Main Service:\n" \
                   f"Robots: none"