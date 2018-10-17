# Напишите функцию, которая по введенному радиусу возвращает площадь поверхности шара и его объем.
# Площадь поверхности = 4*pi*r**2, объем = 4/3*pi*r**3.
# Число pi можно найти в модуле math.
import math

r = float(input('Введите значение r\n'))

def formula_calculation(r):
    s = 4 * math.pi * r ** 2
    v = 4/3 * math.pi * r ** 3
    print('Radius of sphere:', r)
    print('Surface Area is:', s)
    print('Volume is:', v)
formula_calculation(r)
