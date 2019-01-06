from sms.ASmsSender import ASmsSender


class SmsRu(ASmsSender):
    def __init__(self, app_id: str, url='http://sms.ru/sms/send'):
        self.__app_id = app_id
        self.__url = url

    def send(self, number, text):
        raise NotImplementedError("To be implemented")
