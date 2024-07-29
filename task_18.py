a = int(input("Введите номер четверти:"))
if a > 0 and a < 5:
    if a == 1:
        print('x > 0 ; y > 0')
    if a == 2:
        print('x < 0 ; y > 0')
    if a == 3:
        print('x < 0 ; y < 0')
    if a == 4:
        print('x > 0 ; y < 0')