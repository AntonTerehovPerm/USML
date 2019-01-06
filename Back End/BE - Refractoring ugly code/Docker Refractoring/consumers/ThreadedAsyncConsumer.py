from threading import Thread
from abc import abstractmethod

from AsyncConsumer import AsyncConsumer


class ThreadedAsyncConsumer(AsyncConsumer, Thread):
    def __init__(self, connection_params, queue_name):
        super().__init__(connection_params, queue_name)
        Thread.__init__(self)

    def run(self):
        super().run()

    @abstractmethod
    def process_message(self, channel, basic_deliver, properties, body):
        pass
