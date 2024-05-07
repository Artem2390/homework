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

contact2 = Contact("Сидоров", "Олег", 28, "555555555", "sidorov@example.com")
update_contact2 = UpdateContact("Коваленко", "Марія", 32, "777777777", "kovalenko@example.com", "бухгалтер")

# Використання функцій isinstance() та issubclass()
print("Перевірка класів екземплярів:")
print(isinstance(contact1, Contact))
print(isinstance(update_contact1, UpdateContact))
print(isinstance(contact2, UpdateContact))
print(isinstance(update_contact2, Contact))

print("\nПеревірка класу-нащадка:")
print(issubclass(UpdateContact, Contact))
print(issubclass(Contact, UpdateContact))
