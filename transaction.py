class Transaction:
    def __init__(self, amount=None, timestamp=None, from_id=None, to_id=None, transaction_dict=None, account_username=None):
        if transaction_dict is not None:
            self.amount = transaction_dict['Amount']
            self.timestamp = transaction_dict['Datetime']
            self.from_id = transaction_dict['FromID']
            self.to_id = transaction_dict['ToID']
            self.tx_id = transaction_dict['ID']
        else:
            if amount is None or timestamp is None or from_id is None or to_id is None:
                raise TypeError('__init__() missing positional argument!')
            else:
                self.amount = amount
                self.timestamp = timestamp
                self.from_id = from_id
                self.to_id = to_id

        self.account_username = account_username

    def get_amount(self):
        return self.amount

    def get_timestamp(self):
        return self.timestamp

    def get_sender(self):
        return self.from_id

    def get_receiver(self):
        return self.to_id

    def post(self, database_connector):
        query = f'INSERT INTO transactions (Datetime, Amount, FromID, ToID) VALUES ({self.timestamp}, {self.amount}, {self.from_id}, {self.to_id});'
        res = database_connector.execute_query(query)
        return res

    def get_receiver_account(self, accounts_manager):
        acc = accounts_manager.fetch_account(self.to_id)
        return acc

    def get_sender_account(self, accounts_manager):
        acc = accounts_manager.fetch_account(self.from_id)
        return acc

    def json(self, accounts_manager=None):
        if accounts_manager is None:
            return {'timestamp': self.timestamp, 'amount': self.amount, 'from': self.from_id, 'to': self.to_id}
        else:
            sender_acc = self.get_sender_account(accounts_manager)
            receiver_acc = self.get_receiver_account(accounts_manager)

            if sender_acc.username == self.account_username:
                sender_type = sender_acc.type
                receiver_name = receiver_acc.username
            if receiver_acc.username == self.account_username:
                receiver_name = receiver_acc.type
                sender_type = sender_acc.username

            if receiver_acc.username == sender_acc.username:
                sender_type = sender_acc.type
                receiver_name = receiver_acc.type

            return {'timestamp': self.timestamp, 'amount': self.amount, 'from': self.from_id, 'to': self.to_id,
                    'sender_type': sender_type, 'receiver_name': receiver_name}

    def __eq__(self, other):
        return other and self.tx_id == other.tx_id

    def __hash__(self):
        return self.tx_id
