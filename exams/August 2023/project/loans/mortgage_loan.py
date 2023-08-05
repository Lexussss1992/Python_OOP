from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    def __init__(self, interest_rate: float = 3.5, amount: float = 50000):
        super().__init__(interest_rate, amount)

    def increase_interest_rate(self):
        self.interest_rate += 0.5