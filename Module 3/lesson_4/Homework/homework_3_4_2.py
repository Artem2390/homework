class Employee:
    def __init__(self, first_name, last_name, department, start_year):
        if not first_name or not last_name or not department or not str(start_year).isdigit() or start_year < 1900:
            raise ValueError("Неправильні дані про співробітника")
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_year = start_year


employees = []

while True:
    try:
        first_name = input("Введіть ім'я співробітника: ")
        if first_name.lower() == 'q':
            break
        last_name = input("Введіть прізвище співробітника: ")
        department = input("Введіть відділ співробітника: ")
        start_year = int(input("Введіть рік початку роботи співробітника: "))

        employee = Employee(first_name, last_name, department, start_year)
        employees.append(employee)
    except ValueError as e:
        print("Помилка: ", e)

filter_year = int(input("Введіть рік для фільтрації співробітників: "))

print("Співробітники, які були прийняті після року", filter_year)
for employee in employees:
    if employee.start_year > filter_year:
        print(f"{employee.first_name} {employee.last_name} ({employee.department}) - {employee.start_year}")
