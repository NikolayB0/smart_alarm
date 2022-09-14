from smartalarm.sclock import SClock
import time

sc = SClock()
sc.getDateTimeOnline()
while True:
    sc.appendTime()
    print(sc.showTime())
    time.sleep(1)
