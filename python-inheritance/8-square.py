"""
This module defines a class Square that inherits from Rectangle.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class represents a square shape with a single side length 'size'.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string in the format "[Square] <width/height>".
        """
        return "[Square] {}/{}".format(self.width, self.height)
