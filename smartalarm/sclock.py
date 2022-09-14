import ntplib
from datetime import datetime, timedelta
import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
)


class SClock:
    def __init__(self):
        self.current_dateTime: datetime = None

    def getDateTimeOnline(self) -> None:
        try:
            client = ntplib.NTPClient()
            response = client.request("pool.ntp.org")
            Internet_date_time = datetime.fromtimestamp(response.tx_time)
            logging.info("Got time from ntp %s" % Internet_date_time)
            self.current_dateTime = Internet_date_time

        except Exception as Ex:
            logging.error("Could not get time from ntp: %s" % Ex)

    def appendTime(self) -> None:
        self.current_dateTime += timedelta(seconds=1)

    def showTime(self) -> datetime:
        return self.current_dateTime
