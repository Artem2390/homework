username = ("Vlad")
age = 18

# greetings = "Hello, my dear, %s (%s). How are you?" % (username, age)
#
# #.format() style
# greetings = "Hello, my dear, {} ({}). How are you?".format(username, age)
#
# # f"{}, {}" style
# greetings = f"Hello, my dear, {username} ({age}). How are you?"
# print(greetings)


greetings = f"\tHello, my dear, {username} ({age}).\n How are you?"
print("____" * 20)
print(greetings)

print("First symbol:", greetings[12 ])