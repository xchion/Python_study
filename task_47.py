import random

m = int(input('Введите число столбцов: ')) # элементы в подсписке
n = int(input('Введите число линий: ')) # кол-во подсписков

a = [[random.randint(-9, 9) for j in range(m)] for i in range(n)]
print(a)

print('\033[31m', a[0],',', '\033[32m', a[1],',', '\033[33m', a[2],',', '\033[34m', a[3],)
