# Dates

from datetime import timedelta as timedelta
from datetime import date as date
from datetime import time as time
from datetime import datetime as dt

now = dt.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

timestamp = now.timestamp()

print(timestamp)

year_2024 = dt(2024, 1, 1)


print_date(year_2024)


current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)
print(current_date.month)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)

print(year_2024.time())

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=10)

print(end_timedelta - start_timedelta)
print(start_timedelta + end_timedelta)
