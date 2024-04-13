my_tuple = (True, 2, "Hello", 4.7, -5, (6, 7))
print(my_tuple)

print(len(my_tuple))
for i in range(0, len(my_tuple)):
    print(my_tuple[i])

# print(my_tuple[99])
print("Full slice", my_tuple[0:99])

print(">>>", my_tuple[-1][1])

print("Slice", my_tuple[1:3])

print("Slice", my_tuple[1::2])
reverse_tuple = tuple(reversed(my_tuple))
print(f"reverse {reverse_tuple}")