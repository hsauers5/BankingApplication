from account import Account


class AccountsManager:
    def __init__(self, database_connector):
        self.database_connector = database_connector

    def fetch_accounts(self, username):
        query = f'SELECT * FROM accounts WHERE Username = "{username}";'
        res = self.database_connector.execute_query(query)
        accounts = [Account(acc) for acc in res]

        return accounts

    def fetch_account(self, account_id):
        query = f'SELECT * FROM accounts WHERE ID = {account_id}'
        res = self.database_connector.execute_query(query)
        accounts = [Account(acc) for acc in res]

        if not accounts:
            return None
        else:
            return accounts[0]

    def fetch_account_balance(self, username, account_type):
        accounts_data = self.fetch_accounts(username)
        for account in accounts_data:
            if account.type == account_type:
                return account.balance

        return False

    def user_has_account(self, username, account_id):
        accounts = self.fetch_accounts(username)
        for account in accounts:
            if account.id == int(account_id):
                return True

        return False

    def account_has_sufficient_funds(self, account_id, amount):
        acct = self.fetch_account(account_id)
        if amount <= acct.balance:
            return True
        else:
            return False
