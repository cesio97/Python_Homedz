# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


k = int(input("Введите число k: "))


def get_fibonacci(k):
    fibo_numbers = []
    a, b = 1, 1
    for i in range(k):
        fibo_numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k + 1):
        fibo_numbers.insert(0, a)
        a, b = b, a - b
    return fibo_numbers

fibo_numbers = get_fibonacci(k)
print(get_fibonacci(k))