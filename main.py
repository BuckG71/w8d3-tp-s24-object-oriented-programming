"""Main logic of the program"""
import random
from classes import Circle, Rectangle, Triangle

shape_colors = [
    "purple",
    "yellow",
    "blue",
    "orange",
    "pink",
    "chartreuse"
    ]

def rand_color():
    return shape_colors[random.randint(0,len(shape_colors)-1)]

def get_random():
    return random.uniform(1, 10)

def get_valid_triangle():
    # Generate first 2 sides as random
    side1 = get_random()
    side2 = get_random()
    # Generate 3rd side; can't be < absolute difference between s1 & s2, and can't be > s1 + s2 
    min_side3 = abs(side1 - side2) + 0.1
    max_side3 = side1 + side2 - 0.1

    side3 = random.uniform(min_side3, max_side3)

    return side1, side2, side3

def main():
    # Create instances of each type of shape
    my_shapes = [
        Circle(rand_color(), get_random()),
        Circle(rand_color(), get_random()),
        Rectangle(rand_color(), get_random(), get_random()),
        Rectangle(rand_color(), get_random(), get_random()),
        Triangle(rand_color(), *get_valid_triangle()),
        Triangle(rand_color(), *get_valid_triangle())
    ]

    # Iterate over list of shapes, calling methods on each element
    # Illustrates polymorphism by calling the method on the proper class
    for shape in my_shapes:
        print(f"The area of the {shape.color} {shape.type} is {shape.calculate_area():.2f}, and its perimeter is {shape.calculate_perimeter():.2f}.")

if __name__ == "__main__":
    main()
