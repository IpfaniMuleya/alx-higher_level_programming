#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square. Default is 0.
        - position (tuple): The position of the square. Default is (0, 0).
        Raises:
        - TypeError: If size is not an integer or position is not a tuple.
        - ValueError: If size is less than 0 or position has negative integers.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
        - int: The size of the square.

        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Parameters:
        - value (int): The size to set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position attribute.

        Returns:
        - tuple: The position of the square.

        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method to set the position attribute

        Parameters:
        - value (tuple): The position to set.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        - ValueError: If value has negative integers.

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Computes and returns the current square area.

        Returns:
        - int: The area of the square.

        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character # and position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
