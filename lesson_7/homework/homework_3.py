def unique_values_in_list(list1, list2):
    unique_list1 = list(set(list1) - set(list2))
    unique_list2 = list(set(list2) - set(list1))
    return unique_list1, unique_list2


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

unique_list1, unique_list2 = unique_values_in_list(list1, list2)

print("Unique values in list1 (not in list2):", unique_list1)
print("Unique values in list2 (not in list1):", unique_list2)
