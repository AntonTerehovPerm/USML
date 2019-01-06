from sms.ASmsSender import ASmsSender


class NullSmsSender(ASmsSender):
    def send(self, **kwargs):
        pass
