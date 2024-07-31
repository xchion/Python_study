import random
# a = []
# lenght = int(input("Введите длину диапозона:"))
# beginnig = int(input("Введите начало границы значений:"))
# end = int(input("Введите конец границы значений:"))
#
# for i in range(1, lenght + 1):
#     a.append(random.randint(beginnig, end))
# print(a)

coolnames = ['Валя', 'Олег', 'Соня', 'Максим', 'Шарик', 'Какое-то крутое имя', 'Кшыштов']
peculiarities = ['с розой в руке', ', играющий(ая) на компьютере', 'обыкновенный(ая)', 'под зонтиком', 'и 1001 собака', 'в шляпе']
dic1 = random.choice(coolnames)
dic2 = random.choice(peculiarities)
print(dic1, dic2)