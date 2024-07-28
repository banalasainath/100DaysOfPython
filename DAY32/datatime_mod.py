import datetime as dt

# from the datetime class, calling now method which will get the current time from the system
# And the now is of type datetime
now = dt.datetime.now()
# print(type(now))

year = now.year
month = now.month
day = now.weekday()
hour = now.hour
# print(hour)

# Creating a custom date and time variable
date = dt.datetime(year=2001,month=12,day=26,hour=14)
print(date)