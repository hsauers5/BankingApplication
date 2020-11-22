class Transaction:
    def __init__(self, amount=None, timestamp=None, from_id=None, to_id=None, transaction_dict=None):
        if transaction_dict is not None:
            self.amount = transaction_dict['Amount']
            self.timestamp = transaction_dict['Datetime']
            self.from_id = transaction_dict['FromID']
            self.to_id = transaction_dict['ToID']
        else:
            if amount is None or timestamp is None or from_id is None or to_id is None:
                raise TypeError('__init__() missing positional argument!')
            else:
                self.amount = amount
                self.timestamp = timestamp
                self.from_id = from_id
                self.to_id = to_id

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

    def json(self):
        return {'timestamp': self.timestamp, 'amount': self.amount, 'from': self.from_id, 'to': self.to_id}