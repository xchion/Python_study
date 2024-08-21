import itertools
# def dif(num):
#     for i in str(num):
#         v = 0
#         if str(num[i]) != str(num[i + 1]):
#             v += 1
#     if num[0] != num[-1]:
#         v += 1
#     if v == len(num):
#         print("Все элементы разные")
#
# x = dif(465)
# print(x)

# n = int(input("Введите кол-во разрядов в числе: "))
#
# for e in range( 10 ** ( n - 1), (10 ** n) - 1):
# for e in a:
#     k = 0
#     if e % 5 == 0:
#         if
#         print(k)
#     else:
#         print(' Число не подходит ')

k = 0
for x in (0, 10000, 5):
    if len(str(x)) == len(set(str(x))):
        k+=1
print(k)
