# Input values for the list
values = input("Enter the values of the list separated by spaces: ")
numbers = list(map(int, values.split()))

# Find the largest and smallest elements
largest = max(numbers)
smallest = min(numbers)

# Calculate the sum and arithmetic mean
total_sum = sum(numbers)
mean = total_sum / len(numbers)

# Output the results
print(f"Largest element: {largest}")
print(f"Smallest element: {smallest}")
print(f"Sum of elements: {total_sum}")
print(f"Arithmetic mean: {mean}")
