"""Sclock"""
import sys
from datetime import datetime, timedelta
import logging
import ntplib


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
)


class SClock:
    """Class to manage the clocks"""

    def __init__(self):
        self.current_datetime: datetime = None

    def get_datetime_online(self) -> None:
        """Queries ntp to get current time"""
        try:
            client = ntplib.NTPClient()
            response = client.request("pool.ntp.org")
            internet_date_time = datetime.fromtimestamp(response.tx_time)
            logging.info("Got time from ntp %s", internet_date_time)
            self.current_datetime = internet_date_time

        except Exception as ex:
            logging.error("Could not get time from ntp: %s", ex)

    def increment_time(self) -> None:
        """Increments time"""

        self.current_datetime += timedelta(seconds=1)

    def get_time(self) -> datetime:
        """Returns current time"""

        return self.current_datetime
