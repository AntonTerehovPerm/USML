import json
import logging
from ThreadedAsyncConsumer import ThreadedAsyncConsumer
from sms.ASmsSender import ASmsSender

LOGGER = logging.getLogger(__name__)


class ConsumerSms(ThreadedAsyncConsumer):
    def __init__(self, queue_name, connection_params, sms_sender: ASmsSender):
        super().__init__(queue_name=queue_name, connection_params=connection_params)
        self.__sms_sender = sms_sender

    def process_message(self, unused_channel, basic_deliver, properties, body):
        LOGGER.info(f"From queue {self.queue_name} processing  message <{body}>")

        message = json.loads(body)
        self.__sms_sender.send(number=message['phone_number'], text=message['text'])
