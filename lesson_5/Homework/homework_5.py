numbers_str = input("Введіть послідовність чисел через пробіл: ")
numbers_list = numbers_str.split()

sorted_tuple = tuple(sorted(numbers_list))

print("Відсортований кортеж у порядку зростання:", sorted_tuple)
