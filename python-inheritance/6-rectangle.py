"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""

class BaseGeometry:
    """
    The BaseGeometry class represents the base geometry with validation methods.
    """

    def area(self):
        """
        Placeholder method for calculating the area of a shape.
        This method should be implemented in child classes.

        Raises:
            NotImplementedError: This method must be implemented in child classes.
        """
        raise NotImplementedError("area() method not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

class Rectangle(BaseGeometry):
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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height