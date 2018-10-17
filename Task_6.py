# Вам на вход подается список пар чисел.
# Проверить, в скольких парах первое число делится на второе без ошибки. Вывести эти пары и их количество.

pairs = [(2, 3), (4, 0), (9, 3)]
counter = []

for item in pairs:
    try:
        if not item[0] / item[1]:
            raise Exception
        else:
            counter.append(item)
            print(counter)

    except Exception:
        print("Devision can't be done", item)
print('There are {} good pairs:'.format(len(counter)), counter)
