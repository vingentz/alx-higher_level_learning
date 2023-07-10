#!/usr/bin/python3

"""8-base_geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry class"""

    def __init__(self, width, height):
        """initialize private attributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
