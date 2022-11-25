# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21
import math

while True:
    point_1 = [int(i) for i in input("Введите координаты x и y первой точки: ").split()]
    point_2 = [int(i) for i in input("Введите координаты x и y второй точки: ").split()]
    if len(point_1) == 2 and len(point_2) == 2:
        break
    else: print("Координаты должны иметь два числа")


print((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)
print(math.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2))