# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from math import sqrt
a1 = float(input('Введите координату точки a1: '))
a2 = float(input('Введите координату точки a2: '))
b1 = float(input('Введите координату точки b1: '))
b2 = float(input('Введите координату точки b2: '))
x = round(sqrt((pow(b1-a1, 2)+pow(b2-a2, 2))), 2)
print('Расстояние между точками равно ', x)