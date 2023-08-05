from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    def __init__(self, interest_rate: float = 1.5, amount: float = 2000):
        super().__init__(interest_rate, amount)

    def increase_interest_rate(self):
        self.interest_rate += 0.2