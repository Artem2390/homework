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


# Виведення всіх методів класу Contact
print("Методи класу Contact:")
for method in dir(Contact):
    if callable(getattr(Contact, method)):
        print(method)

# Виведення всіх методів класу UpdateContact
print("\nМетоди класу UpdateContact:")
for method in dir(UpdateContact):
    if callable(getattr(UpdateContact, method)):
        print(method)
