"""
This module defines a class BaseGeometry with methods for geometry operations.
"""

class BaseGeometry:
    def area(self):
        """
        Raise an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the 'value' argument as an integer.

        Args:
            name (str): The name of the value being validated (a string).
            value: The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
