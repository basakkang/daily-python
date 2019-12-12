from datetime import datetime, timedelta
import pytz

# get current date time
dt = datetime.now()
print(dt)

# timedelta
dt1 = datetime(1992, 5, 15)
td = dt - dt1
print(type(dt), td)

t1 = timedelta(seconds=10)
t2 = timedelta(seconds=20)
t3 = t1 - t2
print(t3)
print(abs(t3))
print(t3.total_seconds())

# format
print(dt.strftime('%Y-%m-%d %H:%M:%S'))

# strptime
print(datetime.strptime('1992-05-15', '%Y-%m-%d'))

print('local:', dt)
tz_Eastern = pytz.timezone('US/Eastern')
datetime_Eastern = datetime.now(tz_Eastern)
print('Eastern:', datetime_Eastern)
