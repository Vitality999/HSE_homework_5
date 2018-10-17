# Напишите функцию, которая показывает, какой день недели будет через 20 дней.

from datetime import datetime, timedelta
import calendar

def weekday20():
    nowDay = datetime.now()
    nextDay = timedelta(days=20)
    val = nowDay + nextDay
    day = datetime.weekday(val)
    nameDay = calendar.day_name[day]
    print(val, nameDay)
weekday20()