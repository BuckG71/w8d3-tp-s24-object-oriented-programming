"""This file contains all of the classes required for the program."""
from abc import ABC, abstractmethod

class Shape(ABC):
    """The parent class of all shapes"""
    def __init__(self, color) -> None:
        self.color = color

    @abstractmethod
    def calculate_area(self):
        """An abstract method to calculate the area of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    @abstractmethod
    def calculate_perimeter(self):
        """An abstract method to calculate the perimeter of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    @abstractmethod
    def get_color(self):
        """An abstract method to get the color of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    @abstractmethod
    def set_color(self):
        """An abstract method to change the color of the shape"""
        raise NotImplementedError("Subclasses should implement this method")
