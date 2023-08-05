from project.clients.student import Student
from project.clients.adult import Adult
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    valid_loans = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    valid_clients = {"Student": Student, "Adult": Adult}
    granted_loans = 0
    granted_sum = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    @staticmethod
    def find_client_by_id(client_id, clients):
        for client in clients:
            if client.client_id == client_id:
                return client

    @staticmethod
    def find_load_by_type(loan_type, loans_list):
        for loan in loans_list:
            if loan.__class__.__name__ == loan_type:
                return loan
    def add_loan(self, loan_type: str):
        if loan_type not in self.valid_loans:
            raise  Exception("Invalid loan type!")

        self.loans.append(self.valid_loans[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.valid_clients:
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(self.valid_clients[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        current_client = self.find_client_by_id(client_id, self.clients)
        if (loan_type == "StudentLoan" and current_client.__class__.__name__ != "Student") or (loan_type == "MortgageLoan" and current_client.__class__.__name__ != "Adult"):
            raise Exception("Inappropriate loan type!")

        current_loan = self.find_load_by_type(loan_type, self.loans)
        self.loans.remove(current_loan)
        current_client.loans.append(current_loan)

        self.granted_loans += 1
        self.granted_sum += current_loan.amount

        return f"Successfully granted {loan_type} to {current_client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        current_client = self.find_client_by_id(client_id, self.clients)
        if not current_client:
            raise Exception("No such client!")

        if current_client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(current_client)
        return f"Successfully removed {current_client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans_num = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                changed_loans_num += 1

        return f"Successfully changed {changed_loans_num} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients_rates_num = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients_rates_num += 1

        return f"Number of clients affected: {changed_clients_rates_num}."


    def get_statistics(self):
        result = [f"Active Clients: {len(self.clients)}"]
        result.append(f"Total Income: {sum([client.income for client in self.clients]):.2f}")
        result.append(f"Granted Loans: {self.granted_loans}, Total Sum: {self.granted_sum:.2f}")
        result.append(f"Available Loans: {len(self.loans)}, Total Sum: {sum([loan.amount for loan in self.loans]):.2f}")
        total_clients_interest_rate = sum([client.interest for client in self.clients])
        if self.clients:
            result.append(f"Average Client Interest Rate: {total_clients_interest_rate / len(self.clients):.2f}")
        else:
            result.append(f"Average Client Interest Rate: 0.00")
        return "\n".join(result)



bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))

print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.clients[0].loans[0].amount)
print(bank.clients[1].loans[0].amount)

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())