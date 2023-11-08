#!/usr/bin/python3
"""
Module with the write_file function
"""


def write_file(filename="", text=""):
    """function that writes or overwrites a file"""
    with open(filename, 'w', encoding='utf=8') as file:
        num_chars_written = file.write(text)
        return num_chars_written
