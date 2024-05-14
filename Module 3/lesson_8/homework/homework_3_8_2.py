import shelve
import string
import random


# Функція для генерації короткого коду
def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(characters, k=6))
    return short_code


# Завантаження бази посилань з файлу
try:
    db = shelve.open('links_db')
    links_db = db.get('links', {})
finally:
    db.close()


# Функція для скорочення посилання
def shorten_link(original_link):
    if original_link in links_db:
        return links_db[original_link]
    else:
        short_code = generate_short_code()
        links_db[original_link] = short_code
        return short_code


# Функція для отримання посилання за коротким кодом
def get_original_link(short_code):
    for original_link, code in links_db.items():
        if code == short_code:
            return original_link
    return None


# Збереження бази посилань на диск
db = shelve.open('links_db')
db['links'] = links_db
db.close()
