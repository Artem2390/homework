import re


def extract_student_data(input_string):
    # Регулярні вирази для різних частин інформації
    name_pattern = r'([A-Z][a-z]+)\s([A-Z][a-z]+)'  # Прізвище та ім'я
    dob_pattern = r'(\d{2}/\d{2}/\d{4})'  # Дата народження у форматі дд/мм/рррр
    email_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'  # Електронна адреса
    review_pattern = r'\"(.*?)\"'  # Відгук, оточений лапками

    # Знаходження відповідних частин рядка
    name_match = re.search(name_pattern, input_string)
    dob_match = re.search(dob_pattern, input_string)
    email_match = re.search(email_pattern, input_string)
    review_match = re.search(review_pattern, input_string)

    # Формування словника з результатами
    data = {}
    if name_match:
        data['last_name'] = name_match.group(1)
        data['first_name'] = name_match.group(2)
    if dob_match:
        data['dob'] = dob_match.group(1)
    if email_match:
        data['email'] = email_match.group(1)
    if review_match:
        data['review'] = review_match.group(1)

    return data


# Приклад використання функції
input_string = 'Doe John 15/08/1990 john.doe@example.com "The courses were very informative and helpful."'
result = extract_student_data(input_string)
print(result)
