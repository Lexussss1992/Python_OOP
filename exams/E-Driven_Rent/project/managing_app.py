from project.user import User


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

    def upload_vehicle(self):


app = ManagingApp()

print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))