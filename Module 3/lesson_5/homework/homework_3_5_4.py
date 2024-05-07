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

# Виведення інформації про класи та їх екземпляри
print("Інформація про клас Contact:")
print(Contact.__dict__)
print("\nІнформація про клас UpdateContact:")
print(UpdateContact.__dict__)

print("\nІнформація про екземпляр Contact:")
print(contact1.__dict__)
print("\nІнформація про екземпляр UpdateContact:")
print(update_contact1.__dict__)

# Видалення атрибуту 'job'
delattr(update_contact1, 'job')

# Повторне виведення інформації про екземпляр UpdateContact після видалення атрибуту 'job'
print("\nІнформація про екземпляр UpdateContact після видалення атрибуту 'job':")
print(update_contact1.__dict__)
