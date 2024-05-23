import re


def extract_data(input_file, output_file):
    # Відкриваємо файли для читання та запису
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # Читаємо вміст файлу
        text = f_in.read()
        # Знаходимо дату народження
        dob = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)
        # Знаходимо телефон
        phone = re.findall(r'\+?\d{2}\s?\(?\d{3}\)?\s?\d{3}\s?\d{2}\s?\d{2}', text)
        # Знаходимо електронну адресу
        email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        # Записуємо знайдені дані до файлу
        f_out.write(f"Дата народження: {dob}\n")
        f_out.write(f"Телефон: {phone}\n")
        f_out.write(f"Електронна адреса: {email}\n")


input_file = "input.txt"
output_file = "output.txt"
extract_data(input_file, output_file)