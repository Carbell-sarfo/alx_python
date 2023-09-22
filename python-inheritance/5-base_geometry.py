"""
This module defines a class BaseGeometry with methods for geometry-related operations.
"""

class BaseGeometry:
    """
    A base class for geometry-related operations.

    Attributes:
        None

    Methods:
        area(self): Raises an exception indicating that 'area()' is not implemented.
        integer_validator(self, name, value): Validates an integer value.

    """
    def area(self):
        """
        This method raises an exception indicating that 'area()' is not implemented.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): A string representing the name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Example usage:
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        # Attempting to call the 'area' method, which raises an exception
        bg.area()
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        # Validating an integer value (no exception is raised)
        bg.integer_validator("my_int", 12)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        # Invalid: 'value' is a string, not an integer
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        # Invalid: 'value' is less than or equal to 0
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))