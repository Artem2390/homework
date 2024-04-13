import math

x = float(input("Введіть значення x від -π до π: "))

if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)
    print(f"Значення функції y = cos(3x) для x = {x} у радіанах: {y}")
else:
    print("Введене значення x не входить у діапазон від -π до π")



