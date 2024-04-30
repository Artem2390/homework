class Car:
    def __init__(self, make, model, year, color):
        self._make = make
        self._model = model
        self._year = year
        self._color = color

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


my_car = Car("Toyota", "Camry", 2020, "Black")

print(my_car.get_make())
print(my_car.get_model())
print(my_car.get_year())
print(my_car.get_color())

my_car.set_color("Red")
print(my_car.get_color())
