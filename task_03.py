s = ["пн","вт","ср","чт","пт","сб","вс"]
x = int(input("Введите день недели:"))
# if x == 1:
#     print("пн")
# if x == 2:
#     print("вт")
# if x == 3:
#     print("ср")
# if x == 4:
#     print("чт")
# if x == 5:
#     print("пт")
# if x == 6:
#     print("сб")
# if x == 7:
#     print("вс")
if (x > 7) or (x < 0) :
    print('Такого дня недели нет')
else:
    print(s[x - 1])