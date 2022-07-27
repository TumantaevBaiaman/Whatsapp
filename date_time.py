import delorean
from datetime import datetime


def time():
    now = datetime.now()
    dt = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
    return int(delorean.Delorean(dt, timezone='UTC').epoch * 1000)