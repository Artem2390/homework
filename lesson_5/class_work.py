# numbers_str = input("Введіть послідовність чисел через пробіл: ")
# numbers_list = numbers_str.split()
# numbers_tuple = tuple(map(int, numbers_list))
#
#
# sorted_tuple = tuple(sorted(numbers_tuple))
#
# print("Відсортований кортеж у порядку зростання:", sorted_tuple)


def analyze_feedback(feedback):
    discount = 0

    words = feedback.split()
    unique_words = set(words)  # використовуємо множину для унікальних слів

    if "меню" in unique_words:
        discount += 5
    if "спортзал" in unique_words:
        discount += 5
    if "обслуговування" in unique_words:
        discount += 5

    if len(feedback) > 60:
        discount += 15

    return discount

feedback = input("Будь ласка, введіть ваш фідбек: ").lower()
discount = analyze_feedback(feedback)

print(f"Загальна знижка на наступне відвідування: {discount}%")

