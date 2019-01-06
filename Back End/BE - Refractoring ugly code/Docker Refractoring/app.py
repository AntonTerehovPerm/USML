# Простой Service Locator
# Для простоты не учитываем в DEV или PROD режиме запущено приложение.

import app_package.AppLoader


def create_new_dn_conn():
    return app_package.AppLoader.AppLoader.init_db()


db = app_package.AppLoader.AppLoader.init_db()

mailer = app_package.AppLoader.AppLoader.init_mailer()

sms_sender = app_package.AppLoader.AppLoader.init_sms_sender(create_new_dn_conn())
