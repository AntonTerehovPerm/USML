from app_package.ADbConnection import ADbConnection
import sqlite3


class SQLiteDbConnection(ADbConnection):
    def __init__(self, db_filename):
        self.__db_filename = db_filename
        self.__conn = sqlite3.connect(self.__db_filename, check_same_thread=False, timeout=3)
        self.__conn.execute("PRAGMA busy_timeout = 10000")

    def exec_sql(self, raw_sql: str, params=()):
        cur = self.__conn.cursor()
        cur.execute(raw_sql, params)
        self.__conn.commit()

    @property
    def cursor(self):
        return self.__conn.cursor()

    def __del__(self):
        self.__conn.close()
