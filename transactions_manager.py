from transaction import Transaction


class TransactionsManager:
    def __init__(self, database_connector, accounts_manager):
        self.database_connector = database_connector
        self.accounts_manager = accounts_manager

    def fetch_all_transactions(self, username):
        accounts = self.accounts_manager.fetch_accounts(username)
        transactions_list = set()
        for account in accounts:
            transactions = self.fetch_account_transactions(account)
            transactions_list.update(transactions)

        return transactions_list

    def fetch_account_transactions(self, account):
        query = f'SELECT DISTINCT * FROM transactions WHERE FromID = {account.id} OR ToID = {account.id}'
        res = self.database_connector.execute_query(query)
        txs = set([Transaction(transaction_dict=t) for t in res])

        return txs

    def send_money(self, amount, timestamp, from_id, to_id):
        transaction = Transaction(amount, timestamp, from_id, to_id)

        # ensure both accounts exist - else, fail
        if self.accounts_manager.fetch_account(from_id) is None or self.accounts_manager.fetch_account(to_id) is None:
            return False

        # ensure not sending to same account
        if from_id == to_id:
            return False

        # add tx record
        transaction.post(self.database_connector)

        # update acct balances
        sender = self.accounts_manager.fetch_account(from_id)
        receiver = self.accounts_manager.fetch_account(to_id)
        new_sender_balance = sender.balance - transaction.amount
        new_receiver_balance = receiver.balance + transaction.amount

        sender.set_balance(new_sender_balance)
        receiver.set_balance(new_receiver_balance)

        sender.update(self.database_connector)
        receiver.update(self.database_connector)

        # success
        return True
