#!/usr/bin/python3

'''define a square class'''


class Square:
    '''square class with a private attribute size'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        '''retrieve attribute'''

        return self.__size

    @size.setter
    def size(self, value):
        """
        modify attribute value

        Args:
            value: sets size to value if int and >= 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''retrieve the attribute'''

        return self.__position

    @position.setter
    def position(self, value):
        """
        modify attribute value

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''calculate square area'''

        return (self.__size * self.__size)

    def my_print(self):
        '''print the square to stdout with ###'''

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end="")
                print()
