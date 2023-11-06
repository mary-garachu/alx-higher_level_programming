#!/usr/bin/python3
"""
Module with BaseGeometry method
"""


class BaseGeometry:
    """ creates a function that raises an Exception with
    the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
