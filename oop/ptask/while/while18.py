'''While18. Дано целое число N (> 0). Используя операции
деления нацело и взятия остатка от деления, найти количество и сумму его цифр.'''


N = int(input())

count = 0
sum_digits = 0
temp = N

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {sum_digits}")