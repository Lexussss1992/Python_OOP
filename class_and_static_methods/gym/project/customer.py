class Customer:
    ID = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

    @staticmethod
    def get_next_id():
        Customer.ID += 1
        return Customer.ID

    def __repr__(self):
        return f'Customer <{Customer.ID}> {self.name}; Address: {self.address}; Email: {self.email}'