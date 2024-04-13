my_name = "Artem"


def display_greeting():
    name = input("Write your name: ")
    if name == "":
        print(f"Hello, {my_name}! Welcome.")
    else:
        print(f"Hello, {name}! Welcome.")


display_greeting()
