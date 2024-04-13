# Function to display the list in reverse order
def display_reverse_order(lst):
    print("List in reverse order:")
    for num in reversed(lst):
        print(num, end=" ")


# Function to display the list in ascending order
def display_ascending_order(lst):
    print("\nList in ascending order:")
    for num in sorted(lst):
        print(num, end=" ")


# Create an empty list
integer_list = []

# Input the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Input the values for the list
for i in range(num_elements):
    value = int(input(f"Enter value {i + 1}: "))
    integer_list.append(value)

# Menu for displaying the list in different orders
while True:
    print("\nMenu:")
    print("1. Display list in reverse order")
    print("2. Display list in ascending order")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        display_reverse_order(integer_list)
    elif choice == "2":
        display_ascending_order(integer_list)
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
