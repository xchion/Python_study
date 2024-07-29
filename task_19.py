# а роза упала на лапу Азора
# x = int(input("Введите пятизначное число:"))
# if x[1]==x[3] and x[0]==x[4]:
#     print("число является палиндромом")
# else:
#     print("не является")
# if (x > 9999) and (x < 1000000):
#     dig1 = x // 10 ** 4
#     dig5 = x % 10
#     dig4 = (x % 100) // 10
#     dig2 = (x // 10 ** 3) % 10
#     if dig1 == dig5 and dig4 == dig2:
#         print("число является палиндромом")
#     else:
#      print("не является")
palindroms = {}
k = 0
for a in range(1000,10000):
    s = str(a)
    if s[0] == s[-1] and s[1] == s[-2]:
        k+=1
        palindroms[s] = k
print(palindroms)
x = str(input("Введите пятизначное число:"))
if len(x)==5:
    x = x[0] + x[1] + x[3] + x[4]
    if x in palindroms:
        print("число является палиндромом")
    else:
        print("число не является палиндромом")
else:
    print("другое количество символов")

