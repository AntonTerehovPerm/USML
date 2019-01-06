import json
import pika


class QueueSender:
    def __init__(self, connection_params):

        if type(connection_params) is dict:
            self.__connection_params = pika.ConnectionParameters(**connection_params)
        elif type(connection_params) is str:
            self.__connection_params = pika.URLParameters(connection_params)
        else:
            raise TypeError(f"Ожидаем set или string. Получили {type(connection_params)}")

    def send(self, queue: str, message):
        connection = pika.BlockingConnection(self.__connection_params)
        channel = connection.channel()
        channel.queue_declare(queue=queue)

        properties = pika.BasicProperties(content_type='application/json')
        channel.basic_publish(exchange='',
                              routing_key=queue,
                              body=json.dumps(message, ensure_ascii=False),
                              properties=properties)
        connection.close()
