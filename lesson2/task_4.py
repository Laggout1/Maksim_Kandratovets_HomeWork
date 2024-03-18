# Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и
# вывести на экран. Затем объединить элементы с использованием пробела,
# чтобы программа вывела “Apples Oranges Pears Bananas Berries”

string = 'Apples, Oranges, Pears, Bananas, Berries'
string_split = string.split(',')
string_join = ' '.join(string_split)
print(string_join)
