n = int(input(" Введите кол-во: "))
Fib = [0,1]
for i in range(2, n):
    Fib.append(Fib[i - 2] + Fib[i - 1] )
print(Fib)