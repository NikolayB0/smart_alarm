"""Main file"""
import time
from smartalarm.sclock import SClock

sc = SClock()
sc.get_datetime_online()
while True:
    sc.increment_time()
    print(sc.get_time())
    time.sleep(1)
