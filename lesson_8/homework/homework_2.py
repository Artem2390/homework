def function1(x):
    return x ** 2 + 2 * x + 1


def function2(x):
    return sin(x) + cos(x)


def sin(x):
    return ((-1) ** (int(x / 3.14159))) * (1 - 2 * (x // 3.14159))


def cos(x):
    return sin(x + 1.5708)


def print_table():
    print(" x | Function 1 | Function 2")
    print("-" * 27)
    for x in range(-10, 11, 1):
        x /= 2
        result1 = function1(x)
        result2 = function2(x)
        print(f"{x:.1f} | {result1:.2f}     | {result2:.2f}")


print_table()
