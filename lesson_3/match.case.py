# switch - case

day = int(input("Week day: "))
# if 7 < day < 1:
#     print("Use numbers from 1 to 7")
#     exit()
#
# if day == 1:
#     print("Monday, start working")
# elif day == 2:
#     print("Tuesday, start working")
# else:
#     print("use numbers")
#     exit()

    
match day:
    case 1:
        print("Monday, start working")
    case 2:
        print("Tuesday, start working")
    case 3:
        print("Monday, start working")
    case 4:
        print("Tuesday, start working")
    case 5:
        print("Monday, start working")
    case 6:
        print("Tuesday, start working")
    case 7:
        print("Monday, start working")
    case _:
        print("use numbers 1 to 7")
        exit()