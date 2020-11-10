from account import Account


class SavingsAccount(Account):
    def __init__(self, balance, id):
        super(SavingsAccount, self).__init__('Savings', balance, id)
