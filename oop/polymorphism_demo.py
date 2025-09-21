import math

class Shape:
    def area(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)
