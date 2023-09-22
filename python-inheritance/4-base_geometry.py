"""
This module defines a class BaseGeometry with a single method.
"""

class BaseGeometry:
    def area(self):
        """
        This method raises an exception indicating that 'area()' is not implemented.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

# Test the BaseGeometry class
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        # Attempting to call the 'area' method, which raises an exception
        bg.area()
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))