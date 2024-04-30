class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


temp = Temperature()

temp.celsius = 25

print("Temperature in Celsius:", temp.celsius)
print("Temperature in Fahrenheit:", temp.fahrenheit)

temp.fahrenheit = 77

print("Temperature in Celsius:", temp.celsius)
print("Temperature in Fahrenheit:", temp.fahrenheit)
