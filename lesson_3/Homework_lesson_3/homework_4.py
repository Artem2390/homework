import math

print("Виберіть операцію: ")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
print("5. Зведення в ступінь")
print("6. Квадратний корінь")
print("7. Кубічний корінь")
print("8. Синус")
print("9. Косинус")
print("10. Тангенс")

choice = input("Ваш вибір (введіть номер операції): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
elif choice in ['6', '7', '8', '9', '10']:
    num = float(input("Введіть число: "))

if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    if num2 == 0:
        result = "Помилка! Ділення на 0 неможливе."
    else:
        result = num1 / num2
elif choice == '5':
    result = num1 ** num2
elif choice == '6':
    result = math.sqrt(num)
elif choice == '7':
    result = num ** (1/3)
elif choice == '8':
    result = math.sin(num)
elif choice == '9':
    result = math.cos(num)
elif choice == '10':
    result = math.tan(num)
else:
    result = "Невірний вибір операції"

print("Результат: ", result)

