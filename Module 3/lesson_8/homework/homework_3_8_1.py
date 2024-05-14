import random

# Генеруємо 10000 випадкових дійсних чисел
random_numbers = [random.uniform(0, 1000) for _ in range(10000)]

# Записуємо числа у файл
with open('random_numbers.txt', 'w') as file:
    for number in random_numbers:
        file.write(str(number) + '\n')

print("Файл 'random_numbers.txt' був успішно створений з 10000 випадковими числами.")


# Читаємо числа з файлу та обчислюємо їхню суму
with open('random_numbers.txt', 'r') as file:
    numbers = [float(line.strip()) for line in file]

sum_numbers = sum(numbers)

print(f"Сума чисел у файлі 'random_numbers.txt' становить: {sum_numbers}")
