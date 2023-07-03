#!/usr/bin/python3

"""Empty class defining Rectangle"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Perimeter of rectangle"""
        if self.___height == 0 or self.___width == 0:
            return 0
        else
            return (self.width + self.height) * 2
