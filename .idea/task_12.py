import random
a = random.randint(1,1000)
b = random.randint(1,1000)
print(a,b)
if b % a == 0:
    print('кратно')
if b == a:
    print("они равны")
else:
    print(b%a)