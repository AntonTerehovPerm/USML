from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class SmsSubscriber(AbstractObserver):
    def __init__(self, phone):
        self.__phone = phone

    def update(self, message):
        print('%s recieved message!' % self.__phone)


class EmailSubscriber(AbstractObserver):
    def __init__(self, email):
        self.__email = email

    def update(self, message):
        print("%s recieved message: %s" % (self.__email, message))
