def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))

        average = calculate_average(num1, num2, num3)
        print("Середнє арифметичне трьох чисел дорівнює:", average)

        choice = input("Ви хочете обчислити середнє значення іншого набору чисел? (y/n): ")
        if choice.lower() != 'y':
            break
    except ValueError:
        print("Будь ласка, введіть дійсні числа.")
