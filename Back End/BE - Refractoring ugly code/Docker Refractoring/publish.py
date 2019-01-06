import random
import sys
import time

from AppConfig import AppConfig
from publishers.QueueSender import QueueSender
from publishers.RandomMessageGenerator import RandomMessageGenerator

generator = RandomMessageGenerator()
sender = QueueSender(AppConfig.RABBITMQ_CONNECTION_PARAMS)

if __name__ == '__main__':
    while True:
        try:
            generated_message = generator.random_message()
            print(*generated_message)
            sender.send(*generated_message)
            sleep_time = random.randint(1, 2)
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            print("Bye")
            sys.exit()
