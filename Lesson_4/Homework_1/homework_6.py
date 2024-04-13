login = "user123"
password = "12345678"
attempts = 3
total_attempts = 3

while attempts > 0:
    input_login = input("Введіть логін: ")
    input_password = input("Введіть пароль: ")

    if input_login == login and input_password == password:
        print(f"Авторизацію успішно пройдено з {total_attempts - attempts + 1} спроби!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Невірний логін або пароль. Залишилося спроб: {attempts}")
        else:
            print(f"Авторизацію не вдалося пройти з {total_attempts} спроби.")
