def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()

    if input_str == input_str[::-1]:
        return True
    else:
        return False


user_input = input("Введіть фразу для перевірки на паліндром: ")

if is_palindrome(user_input):
    print("Введена фраза є паліндромом.")
else:
    print("Введена фраза не є паліндромом.")


