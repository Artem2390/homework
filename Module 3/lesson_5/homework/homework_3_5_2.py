class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"{self.surname} {self.name}, {self.age} років\nМобільний телефон: {self.mob_phone}\nEmail: {self.email}"

    def sent_message(self, message):
        return f"Повідомлення відправлено до {self.surname} {self.name}: {message}"


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"Контакт {self.surname} {self.name} працює на посаді {self.job}"


# Створення екземплярів класів
contact1 = Contact("Іванов", "Петро", 30, "123456789", "ivanov@example.com")
update_contact1 = UpdateContact("Петров", "Олексій", 25, "987654321", "petrov@example.com", "інженер")

# Використання функцій hasattr(), getattr(), setattr(), delattr()
print("До застосування функцій:")
print(hasattr(contact1, 'surname'))
print(getattr(contact1, 'name'))
setattr(contact1, 'age', 35)
print(contact1.age)

print("\nПісля застосування функцій:")
print(hasattr(contact1, 'job'))
print(getattr(contact1, 'job', 'Атрибут не знайдено'))
setattr(contact1, 'job', 'менеджер')
print(contact1.job)

print("\nВидалення атрибуту 'job' у класі UpdateContact:")
print(hasattr(update_contact1, 'job'))
delattr(update_contact1, 'job')
print(hasattr(update_contact1, 'job'))
