class User:
    def __init__(self, username, id, password_hash, token, accounts):
        self.username = username
        self.id = id
        self.password_hash = password_hash
        self.token = token
        self.accounts = accounts

    def check_balances(self):
        pass

    def fetch_transactions(self):
        pass

    def send_money(self, amount, from_account, receiver_id, to_account):
        pass