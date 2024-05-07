def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль!")
        return None


def power(x, y):
    try:
        result = x ** y
        return result
    except ZeroDivisionError:
        print("Помилка: Зведення нуля в негативний степінь!")
        return None


while True:
    operation = input("Виберіть операцію (+, -, *, /, ** або q для виходу): ")

    if operation == 'q':
        print("Програма завершена.")
        break

    if operation not in ['+', '-', '*', '/', '**']:
        print("Некоректна операція. Спробуйте ще раз.")
        continue

    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if operation == '+':
            print("Результат:", add(num1, num2))
        elif operation == '-':
            print("Результат:", subtract(num1, num2))
        elif operation == '*':
            print("Результат:", multiply(num1, num2))
        elif operation == '/':
            result = divide(num1, num2)
            if result is not None:
                print("Результат:", result)
        elif operation == '**':
            result = power(num1, num2)
            if result is not None:
                print("Результат:", result)

    except ValueError:
        print("Некоректні дані. Спробуйте ще раз.")
