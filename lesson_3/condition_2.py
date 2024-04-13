x = input("Select number: ")
x = int(x)
condition = x > 11 < 111
print("x>10? : ", condition)
secret_code = 20
if condition:
    print("Welcome to 'if' statement")
    if x == secret_code:
        print("You found secret code")
    else:
        print("Try to found secret code")
        if x > secret_code:
            print("Less")
        else:
            print("More")
else:
    print("Welcome to 'else' statement")