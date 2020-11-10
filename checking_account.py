from account import Account


class CheckingAccount(Account):
    def __init__(self, balance, id):
        super(CheckingAccount, self).__init__('Checking', balance, id)
