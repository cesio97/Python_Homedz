# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Ввожу: 'ываабв лповап абвцукв алоабвабв ываываыв'

txt = input("Введите текст через пробел:\n")

find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

