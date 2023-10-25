#!/usr/bin/python3
"""Square generation module for Python project 0x06
"""


class Square:
    """class defined for square generation
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calulates area of square.
        """
        area = self.__size * self.__size

        return area
