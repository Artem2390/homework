from math import pi, e

number = 5
repeat = int(input('Введіть кількість повторів: '))
print(number * repeat)
print(pi * number * repeat)
print(e * 2)

while number >= 0:
    number -= 1

str_1 = 'my string'
sum_1 = 0

for elem in str_1:
    sum_1 += pow(str_1.find(elem), 2)
    print("sum=", sum_1)


def my_function(atr=1):
    print('atr', atr)


my_function(atr=5)
