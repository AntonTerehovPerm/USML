from AppConfig import AppConfig
from app_package.SQLiteDbConnection import SQLiteDbConnection
from lib.mailer.NullMailer import NullMailer
from lib.mailer.SMTPMailer import SMTPMailer
from lib.sms.DbSmsSender import DbSmsSender
from lib.sms.SmsRu import SmsRu


class AppLoader:

    @staticmethod
    def init_db():
        return SQLiteDbConnection(AppConfig.DB_PATH)

    @staticmethod
    def init_mailer():
        if AppConfig.DEV:
            return NullMailer()
        else:
            return SMTPMailer(email_from=AppConfig.SITE_MAIL, smtp_host=AppConfig.SMTP_HOST)

    @staticmethod
    def init_sms_sender(db_conn=None):
        if AppConfig.DEV:
            return DbSmsSender(db_conn)
        else:
            return SmsRu(AppConfig.SMSRU_APP_ID)
