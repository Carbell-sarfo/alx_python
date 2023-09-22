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

        Raises:
            ValueError: If width or height is less than or equal to 0.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        self.width = width
        self.height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

class Square(Rectangle):
    """
    The Square class represents a square shape with a single side length 'size'.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is less than or equal to 0.
        """
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        super().__init__(size, size)

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width