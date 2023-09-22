"""
This module defines a class Rectangle that inherits from BaseGeometry.
"""

class BaseGeometry:
    def area(self):
        """
        This method raises an exception indicating that 'area()' is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates an integer value.

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

# Test the BaseGeometry class
if __name__ == "__main__":
    bg = BaseGeometry()

    # Valid integer values
    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        # Invalid: 'name' is a string, not an integer
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        # Invalid: 'age' is less than or equal to 0
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        # Invalid: 'distance' is less than or equal to 0
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))