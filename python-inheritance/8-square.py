"""
This module defines a class Square that inherits from Rectangle.
"""

class Rectangle:
    """
    The Rectangle class represents a rectangle shape with a width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

class Square(Rectangle):
    """
    The Square class represents a square shape with equal side lengths.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square, which is used for both width and height.
        """
        super().__init__(size, size)