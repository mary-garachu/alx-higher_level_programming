#!/usr/bin/python3
"""
Module with the method inhertits_from
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
