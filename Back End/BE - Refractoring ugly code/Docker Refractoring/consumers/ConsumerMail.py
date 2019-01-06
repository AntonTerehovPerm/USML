import json
import logging

from ThreadedAsyncConsumer import ThreadedAsyncConsumer
from mailer.AMailer import AMailer

LOGGER = logging.getLogger(__name__)


class ConsumerMail(ThreadedAsyncConsumer):
    def __init__(self, queue_name, connection_params, mailer: AMailer):
        super().__init__(queue_name=queue_name, connection_params=connection_params)
        self.__mailer = mailer

    def process_message(self, unused_channel, basic_deliver, properties, body):
        LOGGER.info(f"From queue {self.queue_name} processing  message <{body}>")

        message = json.loads(body)
        self.__mailer.send(**message)
