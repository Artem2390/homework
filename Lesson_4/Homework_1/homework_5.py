height = int(input("Введіть висоту: "))
width = int(input("Введіть ширину: "))
symbol = "*"
for i in range(height + 1):
    for j in range(width + 1):
        print(symbol, end="")
    print()
