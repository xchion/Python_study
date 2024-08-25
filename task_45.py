import random

a = []
for i in range(0, 5):
    a.append(random.randint(-9, 9))
print(a)

c = []
for x in a:
    c.append(x)
print(c)