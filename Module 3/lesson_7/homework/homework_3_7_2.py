def square_of_even_numbers_generator(input_list):
    for num in input_list:
        if num % 2 == 0:
            yield num ** 2


# Приклад використання:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_generator = list(square_of_even_numbers_generator(my_list))
print(result_generator)


def square_of_even_numbers_loop(input_list):
    result = []
    for num in input_list:
        if num % 2 == 0:
            result.append(num ** 2)
    return result


# Приклад використання:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_loop = square_of_even_numbers_loop(my_list)
print(result_loop)
