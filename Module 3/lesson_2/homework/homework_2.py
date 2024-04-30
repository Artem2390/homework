class GraphicalObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pass


class Rectangle(GraphicalObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")


class Clickable:
    def click(self):
        pass


class Button(Rectangle, Clickable):
    def __init__(self, x, y, width, height, label):
        super().__init__(x, y, width, height)
        self.label = label

    def click(self):
        print(f"Button '{self.label}' clicked")


button = Button(10, 10, 100, 50, "Click Me")
rectangle = Rectangle(50, 50, 80, 40)

button.click()
