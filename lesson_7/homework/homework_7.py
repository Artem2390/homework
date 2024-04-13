class Employee:
    def __init__(self, surname, position, experience, portfolio, efficiency_coefficient, technology_stack, salary):
        self.surname = surname
        self.position = position
        self.experience = experience
        self.portfolio = portfolio
        self.efficiency_coefficient = efficiency_coefficient
        self.technology_stack = technology_stack
        self.salary = salary

    def __str__(self):
        return f"Прізвище: {self.surname}\nПосада: {self.position}\nДосвід роботи: {self.experience}\nПортфоліо: {self.portfolio}\nКоефіцієнт ефективності: {self.efficiency_coefficient}\nСтек технологій: {self.technology_stack}\nЗарплата: {self.salary}\n"


class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_sorted_by_surname(self):
        sorted_employees = sorted(self.employees, key=lambda x: x.surname)
        for employee in sorted_employees:
            print(employee)

    def print_most_efficient_employee(self):
        most_efficient_employee = max(self.employees, key=lambda x: x.efficiency_coefficient)
        print(most_efficient_employee)


def main():
    hr_system = HRSystem()

    while True:
        print("\nМеню:")
        print("1. Додати співробітника")
        print("2. Вивести список співробітників, відсортований за прізвищем")
        print("3. Вивести найефективнішого співробітника")
        print("4. Вийти з програми")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            surname = input("Введіть прізвище співробітника: ")
            position = input("Введіть посаду: ")
            experience = input("Введіть досвід роботи: ")
            portfolio = input("Введіть посилання на портфоліо: ")
            efficiency_coefficient = float(input("Введіть коефіцієнт ефективності: "))
            technology_stack = input("Введіть стек технологій: ")
            salary = float(input("Введіть зарплату: "))

            employee = Employee(surname, position, experience, portfolio, efficiency_coefficient, technology_stack, salary)
            hr_system.add_employee(employee)
            print("Співробітник успішно доданий!")

        elif choice == '2':
            print("\nСписок співробітників, відсортований за прізвищем:")
            hr_system.print_sorted_by_surname()

        elif choice == '3':
            print("\nНайефективніший співробітник:")
            hr_system.print_most_efficient_employee()

        elif choice == '4':
            print("Програма завершує роботу!")
            break

        else:
            print("Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
