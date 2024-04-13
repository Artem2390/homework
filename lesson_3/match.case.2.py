data = input("Name, age, height, weight, description with space: ")
print(data)
transformed_data = data.split()
print(transformed_data)


# name, age, height, weight, description = transformed_data
# print(f"{name=}, f"{age=}", f"{height=}", f"{weight=}", f"{description=}")

match transformed_data:
    case name, age, height, weight, description:
        print(f"My name is {name}....")
    case name, age, height, weight:
        print(f"My name is {name}....")
    case name, age, height:
        print(f"My name is {name}....")
    case name, age:
        print(f"My name is {name}....")
    case _:
        print("Incorrect data")
