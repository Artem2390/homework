url_dict = {}


def shorten_url(original_url, short_url):
    if short_url in url_dict:
        print("Ця коротка назва вже використовується.")
    else:
        url_dict[short_url] = original_url
        print(f"Посилання успішно скорочено. ")


def get_original_url(short_url):
    if short_url in url_dict:
        print("Початкове посилання:", url_dict[short_url])
    else:
        print("Посилання з такою короткою назвою не знайдено.")


while True:
    print("\nМеню:")
    print("1. Скоротити посилання")
    print("2. Отримати початкове посилання за короткою назвою")
    print("3. Вийти")

    choice = input("Оберіть опцію: ")

    if choice == '1':
        original_url = input("Введіть початкове посилання: ")
        short_url = input("Введіть коротку назву: ")
        shorten_url(original_url, short_url)
    elif choice == '2':
        short_url = input("Введіть коротку назву: ")
        get_original_url(short_url)
    elif choice == '3':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
