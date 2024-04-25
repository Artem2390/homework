class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, year={self.year}, price={self.price})"


class CarDealership:
    def __init__(self):
        self.available_cars = []

    def add_car(self, car):
        self.available_cars.append(car)

    def sell_car(self, make, model, year):
        for car in self.available_cars:
            if car.make == make and car.model == model and car.year == year:
                self.available_cars.remove(car)
                return car
        return None


dealership = CarDealership()

car1 = Car("Toyota", "Corolla", 2020, 15000)
car2 = Car("Honda", "Civic", 2019, 18000)

dealership.add_car(car1)
dealership.add_car(car2)

sold_car = dealership.sell_car("Toyota", "Corolla", 2020)
if sold_car:
    print(f"Sold car: {sold_car}")
else:
    print("Car not found or already sold")

print("Available cars:")
for car in dealership.available_cars:
    print(car)
