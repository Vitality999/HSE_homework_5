# Вам на вход подается список пар чисел.
# Проверить, в скольких парах первое число делится на второе без ошибки. Вывести эти пары и их количество.

pairs = [(2, 3), (4, 0), (9, 3)]
counter = []
try:
    for item in pairs:
        if not item[0] / item[1]:
            raise Exception
        else:
            counter.append(item)
            print(counter)

except Exception:
    print("Devision can't be done", item)
