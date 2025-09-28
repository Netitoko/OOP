'''For15°. Дано вещественное число A и целое число N (> 0). Найти A в степени N'''

# Найти A в степени N
A = float(input())
N = int(input())

result = 1
for _ in range(N):
    result *= A

print(f"{A} в степени {N} = {result}")