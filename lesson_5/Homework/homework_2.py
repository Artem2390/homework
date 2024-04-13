def calculate_sequence_sum_and_average(numbers):
    second_number = numbers[1]
    penultimate_number = numbers[-2]
    average = sum(numbers) / len(numbers)

    return second_number + penultimate_number, average


numbers = []

while len(numbers) < 5:
    try:
        number = int(input("Введіть число: "))
        numbers.append(number)
    except ValueError:
        print("Будь ласка, введіть ціле число.")

sequence_sum, sequence_average = calculate_sequence_sum_and_average(numbers)

print(f"Сума другого та передостаннього чисел: {sequence_sum}")
print(f"Середнє арифметичне значення послідовності: {sequence_average}")
