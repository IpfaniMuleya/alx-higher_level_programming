#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int or float): The size of the square. Default is 0.

        Raises:
        - TypeError: If size is not a number.
        - ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
        - int or float: The size of the square.

        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Parameters:
        - value (int or float): The size to set.

        Raises:
        - TypeError: If value is not a number.
        - ValueError: If value is less than 0.

        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the current square area.

        Returns:
        - int or float: The area of the square.

        """
        return (self.__size ** 2)

    def __lt__(self, other):
        """Less than comparison."""
        return (self.area() < other.area())

    def __le__(self, other):
        """Less than or equal to comparison."""
        return (self.area() <= other.area())

    def __eq__(self, other):
        """Equal to comparison."""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Not equal to comparison."""
        return (self.area() != other.area())

    def __gt__(self, other):
        """Greater than comparison."""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Greater than or equal to comparison."""
        return (self.area() >= other.area())
