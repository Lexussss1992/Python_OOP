class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def get_next_id():
        next_id = 1
        if Equipment.id == 1:
            return next_id
        next_id = Equipment.id + 1
        return next_id

    def __repr__(self):
        return f'Equipment <{Equipment.id}> {self.name}'