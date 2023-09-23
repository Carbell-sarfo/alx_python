#!/usr/bin/python3
""" Rectangle Module """

from models.base import Base

class Rectangle(Base):
    """ Rectangle class inheriting from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor for Rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method to calculate and return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Method to display the rectangle using '#' characters, considering x and y """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """ Method to update the attributes using both positional and keyword arguments """
        if args:
            arg_names = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """ Custom string representation for Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

if __name__ == "__main__":
    r1 = Rectangle(2, 3, 2, 2)
    r1.display()
    print(r1)

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
    print(r2)

    print("---")

    r3 = Rectangle(1, 1)
    r3.update(id=10, width=20, height=30, x=40, y=50)
    r3.display()
    print(r3)