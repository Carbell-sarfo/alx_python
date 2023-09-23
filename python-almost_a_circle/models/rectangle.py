"""
This module defines a class Rectangle that inherits from the Base class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, which inherits from the Base class.

    Attributes:
        None

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Constructor for the Rectangle class.

    Private Instance Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the upper-left corner of the rectangle.
        __y (int): Y-coordinate of the upper-left corner of the rectangle.

    Public Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the upper-left corner of the rectangle.
        y (int): Y-coordinate of the upper-left corner of the rectangle.
        id (int): Identifier of the rectangle object.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the upper-left corner of the rectangle (default is 0).
            y (int, optional): Y-coordinate of the upper-left corner of the rectangle (default is 0).
            id (int, optional): Identifier of the rectangle object (default is None).

        """
        super().__init__(id)  # Call the constructor of the Base class with 'id'
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # Private attributes with getters and setters
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

# Example usage:
if __name__ == "__main__":
    r = Rectangle(10, 5, 2, 2)
    print(r.width)  # Should print 10
    print(r.height)  # Should print 5
    print(r.x)  # Should print 2
    print(r.y)  # Should print 2
    print(r.id)  # Automatically assigned id