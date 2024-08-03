from abc import ABC, abstractmethod
import math


# Define the abstract class
class Shape(ABC):

    def __init__(self):
        self.area()

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"This is a shape with area: {self.area()}")


# Define a subclass Circle
class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        print(f"{self.__class__.__name__} implementation of area")


# Define a subclass Rectangle
class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        print(f"{self.__class__.__name__} implementation of area")


# Instantiate the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)
