a = int(input("Введіть коефіцієнт a: "))
b = int(input("Введіть коефіцієнт b: "))
c = int(input("Введіть коефіцієнт c: "))

D = b**2 - 4*a*c

if D >= 0:
    x1 = int((-b - D**0.5) / (2*a))
    x2 = int((-b + D**0.5) / (2*a))
    print("Корені рівняння: x1 =", x1, ';' "x2 =", x2)
else:
    real_part = -b / (2 * a)
    imaginary_part = (-D) ** 0.5 / (2 * a)
    x1 = complex(real_part, imaginary_part)
    x2 = complex(real_part, -imaginary_part)
    print("Корені рівняння: x1 =", x1, ';' "x2 =", x2)

