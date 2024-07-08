"""This file contains all of the classes required for the program."""
import math

class Shape():
    """The parent class of all shapes"""
    def __init__(self, color) -> None:
        self.color = color

    def calculate_area(self):
        """An abstract method to calculate the area of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    def calculate_perimeter(self):
        """An abstract method to calculate the perimeter of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    def get_color(self):
        """A method to get the color of the shape"""
        return self.color

    def set_color(self, color):
        """A method to change the color of the shape"""
        self.color = color
        
class Circle(Shape):
    def __init__(self, color, radius: float) -> None:
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        """A method to calculate the area of the shape"""
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        """A method to calculate the perimeter of the shape"""
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, color, length: float, width: float) -> None:
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        """A method to calculate the area of the shape"""
        return self.length * self.width

    def calculate_perimeter(self):
        """A method to calculate the perimeter of the shape"""
        return 2 * (self.length + self.width)
class Triangle(Shape):
    def __init__(self, color, side1: float, side2: float, side3: float) -> None:
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        """A method to calculate the area of the shape"""
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def calculate_perimeter(self):
        """A method to calculate the perimeter of the shape"""
        return self.side1 + self.side2 + self.side3
