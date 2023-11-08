#!/usr/bin/python3
"""
Module with append function
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
