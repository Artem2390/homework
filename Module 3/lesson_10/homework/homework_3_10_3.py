def print_last_three_chars(sentence):
    # Розбиваємо речення на окремі слова
    words = sentence.split()
    # Проходимо по кожному слову та друкуємо останні 3 символи
    for word in words:
        print(word[-3:])


sentence = input("Введіть речення: ")
print_last_three_chars(sentence)
