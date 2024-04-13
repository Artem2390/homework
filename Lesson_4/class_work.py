"""
login = "user123"
password = "12345678"
attempts = 3
total_attempts = 3
while attempts > 0:
    input_login = input("Введіть логін: ")
    input_password = input("Введіть пароль: ")

    if input_login == login and input_password == password:
        print("Авторизацію успішно пройдено!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Невірний логін або пароль. Залишилося спроб: {attempts}")
        else:
            print(f"Авторизацію не вдалося пройти з {total_attempts} спроби.")
"""


# height = 10
# symbol = "+"
#
# for i in range(height):
#     print(" " * (height - i - 1) + symbol * (2 * i + 1))
#
# for i in range(height - 2, -1, -1):
#     print(" " * (height - i - 1) + symbol * (2 * i + 1))

