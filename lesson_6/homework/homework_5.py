# Create a list of natural numbers
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new list to store odd values from int_list
new_list = [num for num in int_list if num % 2 != 0]

# Get the number of repetitions from the user
num_repetitions = int(input("Enter the number of repetitions for new_list: "))

# Duplicate new_list based on the number of repetitions
duplicated_list = new_list * num_repetitions

# Clear int_list
int_list.clear()

print("Original int_list:", int_list)
print("New list with odd values:", new_list)
print("Duplicated list based on repetitions:", duplicated_list)

