import time

a = int(input("Введите число:"))
k = 0

start = time.time ()
while a > 0:
    c = a % 10
    k = k + c
    a = a // 10
finish = time.time ()
print(finish - start)

print(k)