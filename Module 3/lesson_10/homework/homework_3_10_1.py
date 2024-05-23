import re
from collections import Counter


def count_words(text):
    # Видаляємо зайві символи та перетворюємо текст у нижній регістр
    text = re.sub(r'[^\w\s]', '', text).lower()
    # Розбиваємо текст на окремі слова
    words = re.findall(r'\w+', text)
    # Знаходимо частоту кожного слова
    word_counts = Counter(words)
    return word_counts


text = "Це приклад тексту. Текст містить декілька слів, які повторюються. Слова повторюються, бо це приклад."
word_counts = count_words(text)
print(word_counts)
