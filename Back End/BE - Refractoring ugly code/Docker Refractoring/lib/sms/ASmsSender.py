from abc import ABC, abstractmethod


class ASmsSender(ABC):
    @abstractmethod
    def send(self, number, text):
        pass
