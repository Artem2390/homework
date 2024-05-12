def reverse_generator(input_list):
    for i in range(len(input_list) - 1, -1, -1):
        yield input_list[i]


# Приклад використання:
my_list = [1, 2, 3, 4, 5]
for item in reverse_generator(my_list):
    print(item)
