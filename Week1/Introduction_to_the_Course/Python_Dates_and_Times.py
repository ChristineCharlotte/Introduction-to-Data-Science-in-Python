# Dates and Times

import datetime as dt
import time as tm

time0 = tm.time()
dtnow = dt.datetime.fromtimestamp(time0)
print(dtnow)

print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)

delta = dt.timedelta(days=100)
print('delta', delta)

today = dt.date.today()
print('today - delta: ', today-delta)

print(today > today - delta)
