# time is a built-in module
# time
#  |__ class struct_time with inherited methods from builtins.tuple, builtins.object
#           
#  |__ function ctime
#  |__ function gmtime
#  |__ function localtime

# import functions
from time import ctime   # ctime converts epoch time (ex:1661522400) to string form (Thu Aug 25 16:00:00 2022)
from time import gmtime   # Convert a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero.
from time import localtime # Like gmtime() but converts to local time.

# datetime is a library module of classes
# datetime
#   |__ class datetime
#          |__ method now
#          |__ method timestamp
#          |__ method timedelta
import datetime as dt
#import classes from module
from datetime import datetime, timedelta  # classes of module datetime

# Getting the current date and time
today = dt.datetime.now()  # direct call of a class method

# https://docs.python.org/3/library/time.html?highlight=unix%20epoch%20convert
epoch = gmtime(0)
# gmtime returns time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
print(epoch)


# getting the timestamp method from datetime class
ts = datetime.timestamp(today)  # timestamp is a function of datetime class

print("Date and time is:", today)
print("Timestamp is:", ts)


# adding timedelta
current_date = datetime.now()
print('Given Date:', current_date)

# add 4 weeks in given date
new_date = current_date + timedelta(weeks=4)
print('Future Date:', new_date)