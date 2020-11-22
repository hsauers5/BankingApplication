class Account:
    def __init__(self, account_dict):
        self.type = account_dict['Type']
        self.balance = account_dict['Balance']
        self.id = account_dict['ID']
        self.username = account_dict['Username']

        self.transactions = []

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance
        return self.balance

    def update(self, database_connector):
        query = f'UPDATE accounts SET Type = "{self.type}", Balance = {self.balance}, Username = "{self.username}" WHERE ID = {self.id} ;'
        res = database_connector.execute_query(query)
        return res

    def json(self):
        return {
            'Type': self.type,
            'Balance': self.balance,
            'ID': self.id,
            'Username': self.username
        }
