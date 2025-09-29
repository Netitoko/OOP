'''Даны три числа. Найти среднее из них
(т. е. число, расположенное между наименьшим и наибольшим).'''

# Найти среднее из трех чисел
a = int(input())
b = int(input())
c = int(input())

if a <= b <= c or c <= b <= a:
    middle = b
elif b <= a <= c or c <= a <= b:
    middle = a
else:
    middle = c

print(f"Среднее число: {middle}")