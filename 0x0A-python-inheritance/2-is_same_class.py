#!/usr/bin/python3
"""
Module with the method is_same_class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of class"""
    return type(obj) == a_class
