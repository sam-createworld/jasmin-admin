import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cwt_datamodel.daily_quota import DailyQuota, Base as DailyQuotaBase

from django.conf import settings
from main.core.exceptions import *

from jasmin_web_panel_smpp.users import Users
from jasmin_web_panel_smpp.conn import TelnetConnection


def validate_quota_value(value):
    try:
        int(value)
    except ValueError as e:
        return True if value == 'None' else False

    return True


if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"),
                        format='%(asctime)s %(levelname)-8s %(process)d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    db_path = f'postgresql://{settings.POSTGRES_USERNAME}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}'
    logging.info(f'Connecting to database[{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}]...')

    db = create_engine(db_path)
    Session = sessionmaker(db)
    session = Session()

    DailyQuotaBase.metadata.create_all(db)
    logging.info('Connected')

    conn = TelnetConnection()
    telnet = conn.telnet
    users = Users(telnet)

    update_count = 0

    for quota in session.query(DailyQuota):
        logging.info(f'Update {quota.uid} quota to {quota.daily_quota}')

        if not validate_quota_value(quota.daily_quota):
            logging.error(f'Failed!! Invalid quota value [{quota.daily_quota}]')
            continue

        data = [
            ["mt_messaging_cred", "quota", "sms_count", quota.daily_quota]
        ]

        try:
            users.partial_update(data, quota.uid)
            update_count += 1
        except (UnknownError, JasminError, JasminSyntaxError) as e:
            logging.error(f'Failed!! {e}')
            pass

        if logging.getLogger().isEnabledFor(logging.DEBUG):
            u = users.get_user(quota.uid)
            logging.info(u)

    logging.info(f'Done! Updated daily quota for {update_count} records')

