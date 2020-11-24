import hashlib
from users_manager import UsersManager
import base64


class AuthManager:
    def __init__(self, database_connector, users_manager=None):
        self.database_connector = database_connector

        if users_manager is None:
            self.users_manager = UsersManager(database_connector)
        else:
            self.users_manager = users_manager

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest().upper()

    def compare_hashes(self, hash1, hash2):
        return hash1 == hash2

    def check_token(self, token):
        try:
            decoded_token = base64.b64decode(token).decode('UTF-8')
            username, password = decoded_token.split(':')
        # @TODO
        except:
            return False
        return self.check_auth(username, password)

    def check_auth(self, username, password):
        user = self.users_manager.get_user(username)

        if not user:
            return False

        password_hash = self.hash_password(password)
        expected_hash = user['PasswordHash']

        return self.compare_hashes(password_hash, expected_hash)

    def generate_token(self, username, password):
        return base64.b64encode(f'{username}:{password}'.encode('UTF-8')).decode('UTF-8')

    def get_username_from_token(self, token):
        try:
            decoded_token = base64.b64decode(token).decode('UTF-8')
            username, password = decoded_token.split(':')
            return username

        # @TODO
        except:
            return False
