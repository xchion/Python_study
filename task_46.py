import random

m = int(input('Введите число столбцов: ')) # элементы в подсписке
n = int(input('Введите число линий: ')) # кол-во подсписков

a = [[random.randint(-9, 9) for j in range(m)] for i in range(n)]
print(a)