from mailer.AMailer import AMailer


class NullMailer(AMailer):
    def send(self, **kwargs):
        pass
