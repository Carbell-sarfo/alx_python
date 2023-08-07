class Square:
    """
    This class represents a square shape.

    Attributes:
        __size (int): Private instance attribute to store the size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.

        Note:
            The size parameter is assigned to the private instance attribute __size.
        """
        self.__size = size