from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan
    }

    VALID_CLIENTS = {
        'Student': Student,
        'Adult': Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):

        if loan_type not in self.VALID_LOANS:
            raise Exception('Invalid loan type!')

        self.loans.append(self.VALID_LOANS[loan_type])
        return f'{loan_type} was successfully added.'

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type not in self.VALID_CLIENTS:
            raise Exception('Invalid client type!')

        if self.capacity == 0:
            return 'Not enough bank capacity.'

        self.clients.append(self.VALID_CLIENTS[client_type](client_name, client_id, income))
        self.capacity -= 1
        return f'{client_type} was successfully added.'

    def grant_loan(self, loan_type: str, client_id: str):

        client = [c for c in self.clients if c.client_id == client_id][0]
        loan = [l for l in self.loans if l.__name__ == loan_type][0]

        if loan_type != 'StudentLoan' and client.__class__.__name__ == 'Student':
            raise Exception('Inappropriate loan type!')
        elif loan_type != 'MortgageLoan' and client.__class__.__name__ == 'Adult':
            raise Exception('Inappropriate loan type!')
        elif loan_type == 'MortgageLoan' and client.__class__.__name__ != 'Adult':
            raise Exception('Inappropriate loan type!')
        elif loan_type != 'StudentLoan' and client.__class__.__name__ == 'Student':
            raise Exception('Inappropriate loan type!')
        else:
            [client.loans.append(l) for l in self.loans]
            self.loans.remove(loan)
            return f'Successfully granted {loan_type} to {client.name} with ID {client_id}.'

    def remove_client(self, client_id: str):

        try:
            client = next(filter(lambda x: x.client_id == client_id, self.clients))
        except Exception:
            return 'No such client!'

        if len(client.loans) > 0:
            raise Exception('The client has loans! Removal is impossible!')

        self.clients.remove(client)
        return f'Successfully removed {client.name} with ID {client_id}.'

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__name__ == loan_type:
                for c in self.clients:
                    if loan not in c.loans:
                        loan.increase_interest_rate
                        number_of_changed_loans += 1
            return f'Successfully changed {number_of_changed_loans} loans.'

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1
            return f'Number of clients affected: {changed_client_rates_number}.'

    def get_statistics(self):
        total_clients_count = len(self.clients)
        total_clients_income = 0
        loans_count_granted_to_clients = 0
        granted_sum = 0
        loans_count_not_granted = len(self.loans)
        not_granted_sum = 0
        sum_client_interest_rate = 0
        avg_client_interest_rate = sum_client_interest_rate / len(self.clients)

        for client in self.clients:
            total_clients_income += client.income
            loans_count_granted_to_clients += len(client.loans)
            granted_sum += client.loans.amount
            sum_client_interest_rate += client.interest

        for loan in self.loans:
            not_granted_sum += loan.amount

        """
        "Active Clients: {total_clients_count} 

        Total Income: {total_clients_income} 
        
        Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum} 
        
        Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum} 
        
        Average Client Interest Rate: {avg_client_interest_rate}" 
        :return: 
        """

        res = f"Active Clients: {total_clients_count}\n" \
              f"Total Income: {total_clients_income}\n" \
              f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum}\n" \
              f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum}\n" \
              f"Average Client Interest Rate: {avg_client_interest_rate}"


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

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))

print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))

print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())