class NotificationManager:
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        if subscriber not in self.__subscribers:
            self.__subscribers.add(subscriber)

    def unsubcribe(self, subscriber):
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)

    def notify_subscribers(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)
