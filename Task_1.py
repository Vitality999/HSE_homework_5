# Переведите строку в дату, используя datetime: 2018-08-14T19:00:55Z

from datetime import datetime

date = '2018-08-14T19:00:55Z'
date_new = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
print(date_new)

