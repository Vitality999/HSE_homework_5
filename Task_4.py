# Найти в строке все пароли и вывести их (только численную часть).
# Пароли только числовые, идут после выражения password:. Просто числа паролем не являются.

import re

phrase = 'kasdjvb password:12345 hdhvbpassword:23456, 3534726, password123 fhbfvw'
patterns = r'password:(\d+)'

def find_all_passwords(patterns, phrase):
    result = re.findall(patterns, phrase)
    return result
print(find_all_passwords(patterns, phrase))