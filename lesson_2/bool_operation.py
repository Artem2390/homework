# and - "і"
# or - "або"
# not - "не"

x = 10
y = 20

print(x < y)
print(x <= y)

x = 10
y = 11
a = 10

print(x < y)
print(x <= y)
print(x > y)
print(x >= y)

print(x == y)  # дорівнює
print(x != 10)  # не дорівнює

print(x is a)
print("x:", id(x))
print("a:", id(a))

print(x is not a)

color = "blue"
size = 10
shape = "circle"

print(color == 'red')
print(size > 5)
print(shape != "square")

print("Do we have circle of blue color, with size bigger then 3")
condition = (color == "blue") and shape == "circle" and size > 3

print("Do we have figure of blue color, with size bigger then 10 or at least it is a circle?")
condition = (color == "blue" and size > 15) or shape == "circle" # (False and False) or True -> False or True -> True
print(condition)
