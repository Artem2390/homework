user_input = input("Введіть фразу з 10 символів: ")

if len(user_input) != 10:
    print("Фраза повинна складатися з рівно 10 символів.")
else:
    ascii_sum = 0
    for char in user_input:
        ascii_sum += ord(char)

    print("Сума ASCII-кодів символів у введеному рядку:", ascii_sum)