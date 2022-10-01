# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
a = int(input("Введите число: "))
negofib=[1,-1]
fib=[1,1]
for i in range(2,a):
    list = fib[i-1]+fib[i-2]
    fib.append(list)
    list_negofib = negofib[i-2]-negofib[i-1]
    negofib.append(list_negofib)
negofib.reverse()
negofib.append(0)

print(f"Ответ: {negofib+fib}")