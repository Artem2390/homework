def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    def calc_result(a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b - discriminant ** 0.5) / (2 * a)
            x2 = (-b + discriminant ** 0.5) / (2 * a)
            return [x1, x2]
        elif discriminant == 0:
            x1 = -b / (2 * a)
            return [x1]
        else:
            return []

    return calc_result(a, b, c)


# Get input from the user for coefficients a, b, c
a = float(input("Enter the value of coefficient a: "))
b = float(input("Enter the value of coefficient b: "))
c = float(input("Enter the value of coefficient c: "))

# Calculate the roots of the quadratic equation
roots = quadratic_equation(a, b, c)

# Display the results
if len(roots) == 0:
    print("The quadratic equation has no real roots.")
else:
    print("The roots of the quadratic equation are:", roots)
