import unittest
from account import Account


class AccountTest(unittest.TestCase):
    type = 'a'
    bal = 100
    acc_id = 1234
    username = 'marsellus_wallace'
    account_dict = {
        'Type': type,
        'Balance': bal,
        'ID': acc_id,
        'Username': username
    }

    tx_list = []

    acc = Account(account_dict)

    def test_init(self):
        acc = self.acc

        assert acc.type == self.type
        assert acc.balance == self.bal
        assert acc.id == self.acc_id
        assert acc.username == self.username

    def test_get_balance(self):
        assert self.acc.get_balance() == self.bal

    def test_set_balance(self):
        self.bal = 200
        assert self.acc.set_balance(self.bal) == self.bal
        assert self.acc.get_balance() == self.bal

    def test_update(self):
        class MockConn:
            def __init__(self):
                pass

            def execute_query(self, s):
                return "results"

        conn = MockConn()
        assert self.acc.update(conn) == 'results'

    def test_json(self):
        json = {
            'Type': self.type,
            'Balance': self.bal,
            'ID': self.acc_id,
            'Username': self.username
        }

        assert self.acc.json() == json
