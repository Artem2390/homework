def create_color_tuple(red, green, blue):
    color_tuple = (red, green, blue)
    return color_tuple


try:
    red = int(input("Введіть значення червоного кольору (від 0 до 255): "))
    green = int(input("Введіть значення зеленого кольору (від 0 до 255): "))
    blue = int(input("Введіть значення синього кольору (від 0 до 255): "))

    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        color = create_color_tuple(red, green, blue)
        print("Кортеж з введеним кольором:", color)
    else:
        print("Значення кольору повинні бути в діапазоні від 0 до 255.")
except ValueError:
    print("Будь ласка, введіть цілі числа.")
