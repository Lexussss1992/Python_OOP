class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        hours = hours * 60
        return cls(trainer_id, equipment_id, duration=hours)

    @staticmethod
    def get_next_id():
        next_id = 1
        if ExercisePlan.id == 1:
            return next_id
        next_id = ExercisePlan.id + 1
        return next_id

    def __repr__(self):
        return f'Plan <{ExercisePlan.id}> with duration {self.duration} minutes'