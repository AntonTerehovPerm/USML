from threading import Thread


class ThreadsManager:
    def __init__(self):
        self.__items = list()

    def add(self, item: Thread):
        self.__items.append(item)

    def run_all(self):

        for consumer in self.__items:
            consumer.start()

        for consumer in self.__items:
            consumer.run()

    def stop_all(self):
        for consumer in self.__items:
            consumer.stop()
