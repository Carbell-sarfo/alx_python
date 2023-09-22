"""
This module defines a class Square that inherits from Rectangle.
"""

class Rectangle:
    """
    The Rectangle class represents a rectangle shape with width and height.
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

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.width, self.height)

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
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format "[Square] size/size".
        """
        return "[Square] {}/{}".format(self.width, self.height)