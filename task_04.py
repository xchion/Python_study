x = int(input("Введите число 1:"))
y = int(input("Введите число 2:"))
z = int(input("Введите число 3:"))
a=[]
# if x > y and x > z:
#     print(x)
# if y > x and y > z:
#     print(y)
# if z > y and z > y:
#     print(z)
# else:
#     print('Нет бОльшего числа')
if x == y and y == z and x == z:
    print("Все числа одинаковые")
else:
    a.append(x)
    a.append(y)
    a.append(z)
    print(max(a))


