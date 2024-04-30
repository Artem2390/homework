class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Car(Transport):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Bicycle(Transport):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Bicycle type: {self.type}")


car1 = Car("Toyota", "Camry", 2020, 4)
bicycle1 = Bicycle("Giant", "Talon", 2019, "Mountain")

car1.display_info()
bicycle1.display_info()
