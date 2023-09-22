"""
This module defines a class BaseGeometry with a single method.
"""

class BaseGeometry:
    """
    A base class for geometry-related operations.

    Attributes:
        None

    Methods:
        area(self): Raises an exception indicating that 'area()' is not implemented.

    """
    def area(self):
        """
        This method raises an exception indicating that 'area()' is not implemented.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

# Example usage:
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        # Attempting to call the 'area' method, which raises an exception
        bg.area()
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))