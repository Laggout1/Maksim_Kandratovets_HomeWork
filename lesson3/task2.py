# Определить существование треугольника

a = float(input(' введите первую сторону треугольника '))
b = float(input(' введите вторую сторону треугольника '))
c = float(input(' введите третью сторону треугольника '))
if a + b > c and a + c > b and b + c > a:
    print('мы нашли треугольник')
else:
    print('мы не нашли треугольник')
    