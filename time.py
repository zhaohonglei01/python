
import time

localtime = time.localtime()
print  localtime

localtime2 = time.localtime(time.time())
print  localtime2


localtime3 = time.asctime( time.localtime() )
print localtime3

import calendar
cal=calendar.month(2016,2)
print cal