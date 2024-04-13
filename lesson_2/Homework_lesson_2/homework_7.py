import math


def calculator_circle_area(radius):
    area = math.pi * radius ** 2
    return area


radius = int(input("Введіть радіус кола: "))
area = calculator_circle_area(radius)
rounded_area = round(area, 1)

print("Площа кола з радіусом", radius, "дорівнює", rounded_area)