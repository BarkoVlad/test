import math
s = int(input('Введите длину стороны : '))
n = int(input('Введите количество сторон : '))
s = float(s)
n = float(n)
tg = math.sqrt(2 * s + 2 * n )
square = (s * n) / 2
p = s + n + tg
print(square, "Площадь многоугольника : ")
print(p, "Периметр многоугольника : ")