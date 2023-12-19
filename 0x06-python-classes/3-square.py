#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square. Default is 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes and returns the current square area.

        Returns:
        - int: The area of the square.

        """
        return (self.__size ** 2)
