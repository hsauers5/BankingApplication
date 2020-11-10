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

    def get_transactions(self):
        return self.transactions

    def set_transactions(self, transactions):
        self.transactions.extend(transactions)
        return self.transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return self.transactions

    # @TODO
    def post(self, database_connector):
        pass

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
