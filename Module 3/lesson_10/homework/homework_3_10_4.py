def analyze_text(text):
    # Розбиваємо текст на окремі слова
    words = text.split()
    # Знаходимо унікальні слова
    unique_words = set(words)
    # Виводимо унікальні слова на екран
    print("Унікальні слова:")
    for word in unique_words:
        print(word)
    # Знаходимо загальну кількість слів та кількість унікальних слів
    total_words = len(words)
    unique_words_count = len(unique_words)
    # Виводимо кількість слів на екран
    print(f"Загальна кількість слів: {total_words}")
    print(f"Кількість унікальних слів: {unique_words_count}")


text = "Це приклад тексту. Текст містить декілька слів, які повторюються. Слова повторюються, бо це приклад."
analyze_text(text)
