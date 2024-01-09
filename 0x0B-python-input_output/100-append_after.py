#!/usr/bin/python3
"""
Module for appending text after lines containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after lines
                         containing the search string.
    """
    with open(filename, mode='r') as file:
        lines = file.readlines()

    with open(filename, mode='w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
