class Transaction:
    def __init__(self, transaction_dict):
        self.amount = transaction_dict['Amount']
        self.timestamp = transaction_dict['Timestamp']
        self.from_id = transaction_dict['FromID']
        self.to_id = transaction_dict['ToID']

    def __init__(self, amount, timestamp, from_id, to_id):
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
