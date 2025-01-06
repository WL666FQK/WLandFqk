class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def print_area(shape):
    print("The area of the shape is:", shape.area())


circle = Circle(5)
rectangle = Rectangle(10, 5)

print_area(circle)
print_area(rectangle)
