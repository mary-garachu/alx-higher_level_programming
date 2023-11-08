#!/usr/bin/python3
"""
Module with the function read_file
"""


def read_file(filename=""):
    """function that reads through a file"""
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
