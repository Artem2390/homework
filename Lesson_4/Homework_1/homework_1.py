a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

if a < b:
    numbers_list = list(range(a, b+1))
    print("Список всіх натуральних чисел від", a, "до", b, ":", numbers_list)

    sum = (b - a + 1) * (a + b) // 2
    print("Сума всіх натуральних чисел від", a, "до", b, "дорівнює", sum)
else:
    print("Перше число має бути менше за друге число!")