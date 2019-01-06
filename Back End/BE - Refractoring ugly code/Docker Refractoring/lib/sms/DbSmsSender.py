from sms.ASmsSender import ASmsSender


class DbSmsSender(ASmsSender):
    def __init__(self, database_connection):
        self.__db = database_connection

    def send(self, number, text):
        sql = """
                INSERT INTO {0}({1}, {2}) VALUES (?, ?);
                """.format('sms', 'phone_number', 'message')

        self.__db.exec_sql(sql, (number, text))
