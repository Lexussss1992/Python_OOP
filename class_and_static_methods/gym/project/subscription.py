class Subscription:
    id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

    @staticmethod
    def get_next_id():
        next_id = 1
        if Subscription.id == 1:
            return next_id
        next_id = Subscription.id + 1
        return next_id

    def __repr__(self):
        return f'Subscription <{Subscription.id}> on {self.date}'