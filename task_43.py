import math
def x_find ( b1, k1, b2, k2): #находит х точки пересечения 2 прямых
    x = (b2 - b1) / (k1 - k2)
    return x

def y_find ( b1, k1, b2, k2): #находит y точки пересечения 2 прямых
    x = (b2 - b1) / (k1 - k2)
    y = k1 * x + b1
    return y
def find_area (x1, y1, x2, y2, x3, y3): #находит площадь треугольника, что образуют 3 прямые
    lenght_a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    lenght_c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    half_c = lenght_c / 2
    high = math.sqrt(( lenght_a ** 2 ) - ( half_c ** 2 ))
    area = ( lenght_c * high) / 2
    return area

# вводим данные 3 прямых :

b1 = int(input())
k1 = int(input())
b2 = int(input())
k2 = int(input())
b3 = int(input())
k3 = int(input())

# находим х и у 3 прямых :

x_ofa = x_find( b1, k1, b2, k2)
x_ofb = x_find( b3, k3, b2, k2)
x_ofc = x_find( b3, k3, b1, k1)

y_ofa = y_find( b1, k1, b2, k2)
 y_ofb = y_find( b3, k3, b2, k2)
 y_ofc = y_find( b3, k3, b1, k1)

print("Координаты пересечения прямых a и c : ","(",x_ofa, y_ofa, ")") # координаты пересечения конкретных прямых
print(find_area (x_ofa, y_ofa, x_ofb, y_ofb, x_ofc, y_ofc)) # площадь треугольника по заданным значениям ( мне было сложно придумать свои какие-то)