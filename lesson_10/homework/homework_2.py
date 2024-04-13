import math


def addition():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    return num1 + num2


def subtraction():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    return num1 - num2


def multiplication():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    return num1 * num2


def division():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    if num2 == 0:
        return "Помилка! Ділення на 0 неможливе."
    else:
        return num1 / num2


def exponentiation():
    num1 = float(input("Введіть число: "))
    num2 = float(input("Введіть ступінь: "))
    return num1 ** num2


def square_root():
    num = float(input("Введіть число: "))
    return math.sqrt(num)


def cubic_root():
    num = float(input("Введіть число: "))
    return num ** (1 / 3)


while True:
    print("Виберіть операцію: ")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Зведення в ступінь")
    print("6. Квадратний корінь")
    print("7. Кубічний корінь")
    print("8. Завершити програму")

    choice = input("Ваш вибір (введіть номер операції): ")

    if choice == '8':
        break

    if choice == '1':
        result = addition()
    elif choice == '2':
        result = subtraction()
    elif choice == '3':
        result = multiplication()
    elif choice == '4':
        result = division()
    elif choice == '5':
        result = exponentiation()
    elif choice == '6':
        result = square_root()
    elif choice == '7':
        result = cubic_root()
    else:
        result = "Невірний вибір операції"

    print("Результат: ", result)