import unittest
from auth_manager import AuthManager


class MockUsersManager:
    def __init__(self):
        pass

    def get_user(self, username):
        if username != 'harry':
            return None
        else:
            return {
                "Account1ID": 1,
                "Account2ID": 2,
                "Name": "harry sauers",
                "PasswordHash": "C27E5A5B42AD5F7C1204E36DE2C569C37496FC41213960A147BE53B1DF2867FC",
                "Username": "harry"
            }


class AuthManagerTest(unittest.TestCase):
    mgr = AuthManager(None, MockUsersManager())

    def test_hash_password(self):
        pwd = 'Ezekiel2517'
        expected_hash = 'C27E5A5B42AD5F7C1204E36DE2C569C37496FC41213960A147BE53B1DF2867FC'
        actual_hash = self.mgr.hash_password(pwd)

        assert expected_hash == actual_hash

    def test_compare_hashes(self):
        hash1 = 'C27E5A5B42AD5F7C1204E36DE2C569C37496FC41213960A147BE53B1DF2867FC'
        hash2 = 'C27E5A5B42AD5F7C1204E36DE2C569C37496FC41213960A147BE53B1DF2867FC'

        assert self.mgr.compare_hashes(hash1, hash2) is True
        assert self.mgr.compare_hashes(hash1 + '1', hash2) is False

    def test_check_auth(self):
        username = 'harry'
        password = 'Ezekiel2517'

        assert self.mgr.check_auth(username, password) is True
        assert self.mgr.check_auth(username, password + '1') is False
        assert self.mgr.check_auth(username + '1', password) is False

    def test_check_token(self):
        token = 'aGFycnk6RXpla2llbDI1MTc='
        assert self.mgr.check_token(token) is True
        token = 'ZmFrZTpwYXNzd29yZA=='
        assert self.mgr.check_token(token) is False

    def test_generate_token(self):
        username = 'harry'
        password = 'Ezekiel2517'

        test_token = self.mgr.generate_token(username, password)
        real_token = 'aGFycnk6RXpla2llbDI1MTc='

        print(test_token)

        assert test_token == real_token
