# Shape Class Hierarchy Documentation

This document explains the design and usage of the Shape Class Hierarchy in Python. The hierarchy includes a base `Shape` class, which includes one attribute ('color') and has abstract methods for 'calculate_area()' and 'calculate_perimeter()'. There are three sub-classes: `Circle`, `Rectangle`, and `Triangle`. Each sub-class inherits the color attribute from the parent class, and each sub-class has a different implementation of the calculate_area() and calculate_perimeter() methods.

## Class Design

### Shape Class

- **Attributes**: `color`
- **Methods**: `__init__()`, `calculate_area()`, `calculate_perimeter()`, `get_color()`, `set_color()`

### Circle Class

- **Attributes**: `radius`, `type`
- **Methods**: `__init__()`, `calculate_area()`, `calculate_perimeter()`

### Rectangle Class

- **Attributes**: `length`, `width`, `type`
- **Methods**: `__init__()`, `calculate_area()`, `calculate_perimeter()`

### Triangle Class

- **Attributes**: `side1`, `side2`, `side3`, `type`
- **Methods**: `__init__()`, `calculate_area()`, `calculate_perimeter()`