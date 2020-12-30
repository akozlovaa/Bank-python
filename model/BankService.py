class BankService:

    def __init__(self, bank_name=None, maintenance_fee_in_usd=None, plan_name=None, service_term=None, interest_rate_in_percents=None, federal_funds_rate_in_percents=None, discount_rate_in_percents=None, service_type=None, account_balance_in_usd=None):
        self.bank_name = bank_name
        self.maintenance_fee_in_usd = maintenance_fee_in_usd
        self.plan_name = plan_name
        self.service_term = service_term
        self.interest_rate_in_percents = interest_rate_in_percents
        self.federal_funds_rate_in_percents = federal_funds_rate_in_percents
        self.discount_rate_in_percents = discount_rate_in_percents
        self.service_type = service_type
        self.account_balance_in_usd = account_balance_in_usd

    def __del__(self):
        return

    def __str__(self):
        bank_name = 'BankServices name: {}\n'.format(self.bank_name)
        maintenance_fee_in_usd = 'Maintenance fee: {}\n'.format(self.maintenance_fee_in_usd)
        plan_name = 'Plan name: {}\n'.format(self.plan_name)
        service_term = 'Service term: {}\n'.format(self.service_term)
        interest_rate_in_percents = 'Interest rate: {}\n'.format(self.interest_rate_in_percents)
        federal_funds_rate_in_percents = 'Federal funds rate: {}\n'.format(self.federal_funds_rate_in_percents)
        discount_rate_in_percents = 'Discount rate: {}\n'.format(self.discount_rate_in_percents)
        service_type = 'Service type: {}\n'.format(self.service_type)
        account_balance_in_usd = 'Account balance: {}\n'.format(self.account_balance_in_usd)
        return bank_name + maintenance_fee_in_usd + plan_name + service_term + interest_rate_in_percents + federal_funds_rate_in_percents + discount_rate_in_percents + service_type + account_balance_in_usd


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


class Deposit:

    def __init__(self, deposit_amount_in_usd=None):
        self.deposit_amount_in_usd = deposit_amount_in_usd

    def __del__(self):
        return

    def __str__(self):
        deposit_amount_in_usd = f'Deposit amount: {self.deposit_amount_in_usd}'
        return deposit_amount_in_usd


class CheckingAccount:

    def __init__(self, withdrawals_last_month=None):
        self.withdrawals_last_month = withdrawals_last_month

    def __del__(self):
        return

    def __str__(self):
        withdrawals_last_month = f'Withdrawals last month: {self.withdrawals_last_month}'
        return withdrawals_last_month
