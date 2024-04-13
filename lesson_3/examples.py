value = 23
if value is None:
    pass  # TODO: resolve later
else:
    print("value is not None")


arg1 = input("First Number: ")
arg2 = input("Second Number: ")
print(arg1.isnumeric())
print(arg1.isdecimal())
print(arg1.isdigit())

if arg1.isdecimal() and arg2.isdecimal():
    arg1 = float(arg1)
    arg2 = float(arg2)
    operator = input("Select operator (+, -, *, /): ")
    if operator == "+":
        print(arg1 + arg2)
    if operator == "-":
        print(arg1 - arg2)
    if operator == "*":
        print(arg1 * arg2)
    if operator == "/":
        print(arg1 / arg2)
else:
    print("Unknow operator")

