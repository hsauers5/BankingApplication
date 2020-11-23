import os
from sqlalchemy import create_engine, text
import time
from pymysql import OperationalError
from sqlalchemy.exc import OperationalError, ResourceClosedError


class DatabaseConnector:
    def __init__(self, username=None, password=None, db_name=None):
        if username is None:
            username = os.environ['MYSQL_USER']
        if password is None:
            password = os.environ['MYSQL_PASSWORD']
        if db_name is None:
            db_name = os.environ['MYSQL_DATABASE']

        mysql_conn_str = f"mysql+pymysql://{username}:{password}@database:3306/{db_name}"
        print(mysql_conn_str)

        engine = create_engine(mysql_conn_str)
        self.connection = None

        m = 30
        for i in range(0, m):
            try:
                self.connection = engine.connect()
                break
            except OperationalError as e:
                if i == m:
                    print('CANNOT CONNECT!')
                    raise e
                time.sleep(1)

    def execute_query(self, query, count=0):
        res = self.connection.execute(text(query).execution_options(autocommit=True))
        try:
            res = res.fetchall()
            return [dict(row) for row in res]
        except ResourceClosedError:
            return True
        except OperationalError as e:
            if count < 5:
                return self.execute_query(query, count+1)
            else:
                raise e
