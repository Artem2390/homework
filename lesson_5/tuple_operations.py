tuple_methods = dir(tuple())
my_tuple_1 = (1, 4, 2, 3, 4, 7)
my_tuple_2 = tuple([1, 2, 3, 4, 4])

# for method in tuple_methods:
#     print(method)
"""    
count
index
"""
x = my_tuple_1.count(3)
print(x)

a = my_tuple_1.index(4, 2)
print(a)

print("Tuple = Tuple: ", my_tuple_1 + my_tuple_2)
print("Tuple * int: ", my_tuple_1 * 3)
#print("Tuple - Tuple: ", my_tuple_1 - my_tuple_2) Error
print("Length: ", len(my_tuple_1))
print("Max: ", max(my_tuple_1))
print("Min element: ", min(my_tuple_1))


to_find = "Hello"
if to_find in my_tuple_1:
    print("Index (element not in collection): ", my_tuple_1.index("hello"))
else:
    print(f"element {to_find} not have in collection")

# random_tuple = ("a", False, 2, 10, 4)
random_tuple_1 = (False, 2, 10, 4)
# print(">>>", max(random_tuple))
print(">>>", max(random_tuple_1))

# random_tuple_1 = (2, 10, 4, (2, 3, 4))
# print(min(random_tuple_1))

# sorted_tuple = tuple(sorted(my_tuple_1))
sorted_tuple = sorted(my_tuple_1, reverse= True)
print(f"Original: {my_tuple_1} {type(my_tuple_1)}")
print(f"Original: {sorted_tuple} {type(sorted_tuple)}")
