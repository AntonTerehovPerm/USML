from abc import ABC, abstractmethod


class AbstractConsumer(ABC):
    @abstractmethod
    def process_message(self, channel, basic_deliver, properties, body):
        pass

    @property
    @abstractmethod
    def queue_name(self):
        return None

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass
