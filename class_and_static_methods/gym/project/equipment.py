class Equipment:
    ID = 1

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_next_id():
        Equipment.ID += 1
        return Equipment.ID

    def __repr__(self):
        return f'Equipment <{Equipment.ID}> {self.name}'