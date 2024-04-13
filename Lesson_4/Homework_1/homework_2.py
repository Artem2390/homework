def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Введіть число: "))

if number < 0:
    print("Факторіал визначений тільки для невід'ємних цілих чисел.")
elif number == 0:
    print("Факторіал числа 0 дорівнює 1.")
else:
    result = factorial(number)
    print("Факторіал числа", number, "дорівнює", result)
