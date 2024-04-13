a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

if a < b:
    numbers_list = list(range(a, b+1))
    print("Список всіх натуральних чисел від", a, "до", b, ":", numbers_list)

    sum_numbers = (b - a + 1) * (a + b) // 2
    print("Сума всіх натуральних чисел від", a, "до", b, "дорівнює", sum_numbers)

    # average = sum_numbers / len(numbers_list)
    average = (a + b) / 2
    print("Середнє арифметичне всіх натуральних чисел від", a, "до", b, "дорівнює", average)

    # Знаходження суми чисел, які є кратними середньому арифметичному
    sum_multiple = sum(num for num in numbers_list if num % average == 0)
    print("Сума чисел, які є кратними середньому арифметичному, дорівнює", sum_multiple)
else:
    print("Перше число має бути менше за друге число!")
