string_1 = "Hello"
string_2 = "World"
string_3 = "!"


some_float = 9.999
float_as_string = str(some_float)
print(some_float, type(some_float))
concatenation = string_1 + string_2 + string_3
print(concatenation)


numbers_as_text = "123"
print(numbers_as_text, type(numbers_as_text))
print(numbers_as_text.isdigit())
text_as_number = int(numbers_as_text)
print(text_as_number, type(text_as_number))

some_text = "hello world"
print(some_text.upper())

char_collection = "12348912427689"
print(char_collection[0])
print(char_collection[0:3])
print(char_collection[-1])
print(char_collection[:])
print(char_collection[::-1])

print(ord("a"))
print(chr(97))