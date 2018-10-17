# Написать выражение, которое ищет в тексте номера телефонов с таким паттерном: tel = '+7(917)12-345-67'

import re

tel = 'My number is +7(917)12-345-67 or +7(495)36-558-47. Call me!'
number = re.compile("[+]\d{1}[(]\d{3}[)]\d{2}[-]\d{3}[-]\d{2}")
expressions = number.findall(tel)
print(expressions)