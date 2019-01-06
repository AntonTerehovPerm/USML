from abc import ABC, abstractmethod


class AMailer(ABC):
    @abstractmethod
    def send(self, to, subject, body):
        pass
