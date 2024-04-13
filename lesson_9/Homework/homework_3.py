def sum_of_numbers_in_interval(start, end):
    if start > end:
        return 0
    return start + sum_of_numbers_in_interval(start + 1, end)


start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

result = sum_of_numbers_in_interval(start, end)

print("The sum of natural numbers from", start, "to", end, "is:", result)
