def check_name_format(name):
    words = name.split()
    return all(word.istitle() and word.isalpha() for word in words)


full_name = input("Введіть ваше ПІБ: ")

if check_name_format(full_name):
    print("Ваше ПІБ відповідає вимогам: кожне слово починається з великої літери та складається лише з літер.")
else:
    print("Ваше ПІБ не відповідає вимогам.")
