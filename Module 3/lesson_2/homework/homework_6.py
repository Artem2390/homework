from datetime import date


class MyClass1:
    adult_count_ukraine = 0
    adult_count_usa = 0

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @classmethod
    def count_adults_ukraine(cls):
        cls.adult_count_ukraine += 1

    @classmethod
    def count_adults_usa(cls):
        cls.adult_count_usa += 1

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.count_adults_ukraine()
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000)
m_per2.count_adults_ukraine()
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
m_per3.count_adults_usa()
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
m_per4.count_adults_usa()
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))

print("Number of adults in Ukraine:", MyClass1.adult_count_ukraine)
print("Number of adults in USA:", MyClass1.adult_count_usa)
