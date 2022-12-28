#Реализуйте алгоритм перемешивания списка.
# Кроме shuffle ничего пока не придумалось

import random
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"Первоначальный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")