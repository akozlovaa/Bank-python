class Loan:

    def __init__(self, loan_amount_in_usd=None, loan_type=None):
        self.loan_amount_in_usd = loan_amount_in_usd
        self.loan_type = loan_type

    def __del__(self):
        return

    def __str__(self):
        loan_amount_in_usd = f'Loan amount: {self.loan_amount_in_usd}'
        loan_type = f'Loan type: {self.loan_type}'
        return loan_amount_in_usd + loan_type