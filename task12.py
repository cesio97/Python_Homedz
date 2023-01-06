# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];   - [2, 3, 5, 6] => [12, 15]

n = int(input('Введите длину списка: '))
import random
list = []
for i in range(n):
    list.append(random.randint(0,10))
import math
print(list)

newlist=[]
m = math.ceil(n/2)-1

for i in range(math.ceil(n/2)):
    newlist.append(list[i]*list[n-i-1])

print(newlist)
print()
