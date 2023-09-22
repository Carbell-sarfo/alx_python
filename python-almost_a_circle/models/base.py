"""
This module defines a base class, Base, for managing the 'id' attribute in future classes.
"""

class Base:
    """
    Base class for managing the 'id' attribute in future classes.

    Attributes:
        None

    Methods:
        __init__(self, id=None): Constructor for the Base class.

    Class Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of objects created.

    """
    # Private class attribute to keep track of the number of objects created.
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): If provided, assign the 'id' attribute with this value.
                                If not provided, increment '__nb_objects' and assign the new value to 'id'.
        
        """
        if id is not None:
            # If 'id' is provided, assign it directly.
            self.id = id
        else:
            # If 'id' is not provided, increment '__nb_objects' and assign it to 'id'.
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# Example usage:
if __name__ == "__main__":
    b1 = Base()
    print(b1.id)  # Should print 1 (the first object created)

    b2 = Base(10)
    print(b2.id)  # Should print 10 (id provided during object creation)