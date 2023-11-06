#!/usr/bin/python3
"""
Module with the BaseGeometry method
"""


class BaseGeometry:
    """Public instance method: def integer_validator
    (self, name, value): that validates value"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
