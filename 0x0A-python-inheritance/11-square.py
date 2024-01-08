#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a Square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes an instance of Square.

        Parameters:
            - size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
