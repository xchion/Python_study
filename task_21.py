import math
x1 = int(input("Введите 1 число:"))
y1 = int(input("Введите 2 число:"))
z1 = int(input("Введите 1 число:"))
x2 = int(input("Введите 1 число:"))
y2 = int(input("Введите 2 число:"))
z2 = int(input("Введите 2 число:"))
x = x1 - x2
y = y1 - y2
z = z1 - z2
lenght = x ** 2 + y ** 2 + z ** 2
print(math.sqrt(lenght))