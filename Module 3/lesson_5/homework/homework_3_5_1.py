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

# Дослідження стану об'єктів за допомогою атрибутів
print("Інформація про об'єкт Contact:")
print(contact1.__dict__)
print(contact1.__class__)
print(contact1.__class__.__bases__)

print("\nІнформація про об'єкт UpdateContact:")
print(update_contact1.__dict__)
print(update_contact1.__class__)
print(update_contact1.__class__.__bases__)

# Виклик методів
print("\nКонтакт:")
print(contact1.get_contact())
print(contact1.sent_message("Привіт! Як справи?"))

print("\nОновлений контакт:")
print(update_contact1.get_contact())
print(update_contact1.get_message())
