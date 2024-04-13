#  example 1
"""
while True:
    print("Hello User")
    x = input("You question: ")
    if x.lower() == "stop":
        break
    print("Thanks for your question")
"""
#  example 2
""" 
x = 0
while True:
    print(f"{x=}")
   # x += 1
    if x > 10:
        break
    x += 1
"""
#  example 3
"""
x = 0
while x <= 100:
    if x % 2 == 1:
        print(f"Skip {x}")
        x += 1
        continue
    print(f"{x=}")
    x += 1
"""

"""
#break in for loop
for i in range(0, 11):
    if i == 5:
        break
    print(i)
print("Loop 1 finish")

#continue in for loop
for i in range(0, 11):
    if i == 5:
        continue
    print(i)
print("Loop 2 finish")
"""