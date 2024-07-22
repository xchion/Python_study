x = int(input("Введите 1 число:"))
y = int(input("Введите 2 число:"))
if x!=0 and y!=0:
    if x>0 and y>0:
        print("1 четверть")
    if x<0 and y>0:
        print("2 четверть")
    if x<0 and y<0:
        print("3 четверть")
    if x>0 and y<0:
        print("4 четверть")
else:
    print("Вы ввели начало координат")