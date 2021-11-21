import time
from time import strftime
import datetime

time_test = 12345
print(time.strftime("%H:%M:%S", time.gmtime(time_test)))  # The output will be 03:25:45

day_time = 1991695500
print(
    time.strftime("%A, %d, %B, %Y", time.gmtime(day_time))
)  # The output will be Friday, 11, February, 2033

day_time2 = datetime.datetime.now()
print(day_time2.day, day_time2.month, day_time2.year)  # The output will be 21 11 2021

format_date = day_time2.strftime("%A, %d %B %Y %H:%M:%S")
print(format_date)  # The output will be Sunday, 21 November 2021 12:06:15
