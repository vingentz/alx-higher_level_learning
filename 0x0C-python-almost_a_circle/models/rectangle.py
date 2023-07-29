#!/usr/bin/python3

"""Child class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """subclass of class Base, Class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances for class rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # Call super class

    @property
    def width(self):
        """Retrive attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting and validating width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting and validating height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting and validating x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting and validating y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Get area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """print # to the stdout"""
        for _ in range(self.__y):
            print()
        for j in range(self.__height):
            for n in range(self.__width + self.__x):
                if n < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """"overriding __str__()"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """"assigns an argument to each attribute"""
        up = ["id", "width", "height", "x", "y"]
        if (args):
            for j in range(len(args)):
                setattr(self, up[j], args[j])
        else:
            for s in kwargs:
                setattr(self, s, kwargs[s])

    def to_dictionary(self):
        """Returns dict representation of a Rectangle"""
        return {
                "x": self.x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width,
                }
