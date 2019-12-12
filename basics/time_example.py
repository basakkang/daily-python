import datetime
import time

# seconds from epoch
t = time.time()

# local time to string
ct = time.ctime(t)

print(t)
print(ct)

# UTC Coordinated Universal Time
# timezone is offset from UTC

# time as a tuple
# Year
# Month as an integer, ranging between 1 (January) and 12 (December)
# Day of the month
# Hour as an integer, ranging between 0 (12 A.M.) and 23 (11 P.M.)
# Minute
# Second
# Day of the week as an integer, ranging between 0 (Monday) and 6 (Sunday)
# Day of the year
# Daylight savings time as an integer with the following values:
# 1 is daylight savings time.
# 0 is standard time.
# -1 is unknown.

# Fri 13 Dec 2019 12:14:09
time_tuple = (2019, 12, 13, 0, 14, 9, 4, 347, -1)
print(datetime.datetime.fromtimestamp(t).timetuple())

lt = time.localtime(t)
print(lt)

# timezone
lt = time.localtime()
print(lt.tm_zone)
print(lt.tm_gmtoff / 3600)

# asctime() for converting a time tuple or struct_time to a timestamp
print(time.asctime(time.gmtime()))

# strftime() format
print(time.strftime('%Y-%m-%d', lt))
