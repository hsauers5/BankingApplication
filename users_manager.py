class UsersManager:
    def __init__(self, database_connector):
        self.database_connector = database_connector

    def get_user(self, user_id):
        res = self.database_connector.execute_query(f'SELECT * FROM users WHERE Username = "{user_id}";')
        if res:
            return res[0]
        else:
            return None
