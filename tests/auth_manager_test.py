import unittest
from auth_manager import AuthManager


class MockUsersManager:
    def __init__(self):
        pass

    def get_user(self, *args, **kwargs):
        return {
            "Account1ID": 1,
            "Account2ID": 2,
            "Name": "harry sauers",
            "PasswordHash": "76D8E42E1BA899A20C2EA30A35359D5D23ECECABF4F8646BDBCB05DDBEF9A9CB",
            "Username": "harry"
        }


class AuthManagerTest(unittest.TestCase):
    mgr = AuthManager(None, MockUsersManager())

    def test_hash_password(self):
        pwd = 'EnglishMotherfuckerDoYouSpeakIt'
        expected_hash = '76D8E42E1BA899A20C2EA30A35359D5D23ECECABF4F8646BDBCB05DDBEF9A9CB'
        actual_hash = self.mgr.hash_password(pwd)

        assert expected_hash == actual_hash

    def test_compare_hashes(self):
        hash1 = '76D8E42E1BA899A20C2EA30A35359D5D23ECECABF4F8646BDBCB05DDBEF9A9CB'
        hash2 = '76D8E42E1BA899A20C2EA30A35359D5D23ECECABF4F8646BDBCB05DDBEF9A9CB'

        assert self.mgr.compare_hashes(hash1, hash2) is True
        assert self.mgr.compare_hashes(hash1 + '1', hash2) is False

    def test_check_auth(self):
        username = 'harry'
        password = 'EnglishMotherfuckerDoYouSpeakIt'

        assert self.mgr.check_auth(username, password) is True
        assert self.mgr.check_auth(username, password + '1') is False
        assert self.mgr.check_auth(username + '1', password) is False

    def test_check_token(self):
        token = 'aGFycnk6RW5nbGlzaE1vdGhlcmZ1Y2tlckRvWW91U3BlYWtJdA=='
        assert self.mgr.check_token(token) is True
        token = 'ZmFrZTpwYXNzd29yZA=='
        assert self.mgr.check_token(token) is False

    def test_generate_token(self):
        username = 'harry'
        password = 'EnglishMotherfuckerDoYouSpeakIt'

        test_token = self.mgr.generate_token(username, password)
        real_token = 'aGFycnk6RW5nbGlzaE1vdGhlcmZ1Y2tlckRvWW91U3BlYWtJdA=='

        assert test_token == real_token
