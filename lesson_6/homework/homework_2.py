# Input values for the two lists
list1 = input("Enter values for the first list separated by spaces: ").split()
list2 = input("Enter values for the second list separated by spaces: ").split()

# Create unique lists relative to each other without repetitions
unique_list1 = list(set(list1) - set(list2))
unique_list2 = list(set(list2) - set(list1))

# Combine the unique lists
final_list = unique_list1 + unique_list2

# Print the final object in forward order
print("Forward order:", final_list)

# Print the final object in reverse order
print("Reverse order:", final_list[::-1])

# Print the final object in ascending order
print("Ascending order:", sorted(final_list))

# Print the final object in descending order
print("Descending order:", sorted(final_list, reverse=True))
