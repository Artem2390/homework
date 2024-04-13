new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get user input
user_input = int(input("Enter a number to check in the list: "))

if user_input in new_list:
    repetitions = new_list.count(user_input)
    position = new_list.index(user_input)
    print(f"The number {user_input} is found in the list.")
    print(f"Number of repetitions: {repetitions}")
    print(f"Position in the list: {position}")
else:
    print(f"The number {user_input} is not found in the list.")
