import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from validate_email import validate_email

from mailer.AMailer import AMailer


class SMTPMailer(AMailer):
    def __init__(self, email_from, smtp_host):
        self._assert_email(email_from)
        self._email_from = email_from
        self._smtp_host = smtp_host

    def send(self, to: str, subject: str, body: str):
        self._assert_email(to)

        message = MIMEMultipart('alternative')
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = self._email_from
        message['To'] = to

        message_text = MIMEText(body.encode(
            'utf-8'), 'plain', 'utf-8')
        message.attach(message_text)

        s = smtplib.SMTP(self._smtp_host)
        s.sendmail(from_addr=self._email_from, to_addrs=[to], msg=message.as_string())

    @staticmethod
    def _assert_email(email):
        if not validate_email(email):
            raise ValueError(f"invalid e-mail: {email}")
