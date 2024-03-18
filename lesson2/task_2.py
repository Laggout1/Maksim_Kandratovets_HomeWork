#  Вычислить сумму цифр случайного трёхзначного числа

import random
random_number = random.randint(100, 999)
digit_sum = sum(int(digit) for digit in str(random_number))
print('Случайное трехзначное число:', random_number)
print('Сумма цифр числа:', digit_sum)