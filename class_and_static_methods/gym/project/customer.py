class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

    @staticmethod
    def get_next_id():
        next_id = 1
        if Customer.id == 1:
            return next_id
        next_id = Customer.id + 1
        return next_id

    def __repr__(self):
        return f'Customer <{Customer.id}> {self.name}; Address: {self.address}; Email: {self.email}'