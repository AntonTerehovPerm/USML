import logging
from ThreadedAsyncConsumer import ThreadedAsyncConsumer

LOGGER = logging.getLogger(__name__)


class ConsumerOne(ThreadedAsyncConsumer):
    def __init__(self, queue_name, connection_params, database_connection):
        super().__init__(queue_name=queue_name, connection_params=connection_params)
        self.__db = database_connection

    def process_message(self, unused_channel, basic_deliver, properties, body):
        LOGGER.info(f"From queue {self.queue_name} processing  message <{body}>")

        sql = """
        INSERT INTO {0}({1}) VALUES (?);
        """.format('one', 'body')

        self.__db.exec_sql(sql, (body,))
