# 4_1

''' Дан массив целых чисел. Вернуть set из уникальных значений, исключив все
нечетные числа и число 0 (если оно есть). Решить задачу в одну строку:
return …
Формат: list -> set'''

set1 = {n for n in [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 345, 856] if n != 0 and n % 2 != 1}
print(set1)
