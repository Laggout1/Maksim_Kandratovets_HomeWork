# Программа, которая определяет тип треугольника по длинам его сторон.

st1 = float(input("Введите длину первой стороны треугольника: "))
st2 = float(input("Введите длину второй стороны треугольника: "))
st3 = float(input("Введите длину третьей стороны треугольника: "))

if st1 + st2 > st3 and st2 + st3 > st1 and st1 + st3 > st2:
    if st1 == st2 == st3:
        print("Это равносторонний треугольник.")
    elif st1 == st2 or st1 == st3 or st2 == st3:
        print("Это равнобедренный треугольник.")
    else:
        print("Это разносторонний треугольник.")
else:
    print("Треугольник с такими сторонами не существует.")