import json
import logging
import random

from ThreadedAsyncConsumer import ThreadedAsyncConsumer

LOGGER = logging.getLogger(__name__)


class ConsumerThree(ThreadedAsyncConsumer):
    def __init__(self, queue_name, connection_params, database_connection):
        super().__init__(queue_name=queue_name, connection_params=connection_params)
        self.__db = database_connection

    def process_message(self, unused_channel, basic_deliver, properties, body):
        LOGGER.info(f"From queue {self.queue_name} processing  message <{body}>")

        words = json.loads(body)
        cost = len(words) * 0.3
        stats = dict()
        for w in words:
            stats[w] = random.randint(0, 2_000_000)

        stats_json = json.dumps(stats, sort_keys=True)

        sql = """
        INSERT INTO {0} ({1}, {2}, {3}) VALUES (?, ?, ?);
        """.format('three', 'keywords', 'keywords_stats', 'cost')

        self.__db.exec_sql(sql, (body, stats_json, cost))
