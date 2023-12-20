#!/usr/bin/python3

"""Defines a MagicClass"""

import math


class MagicClass:
    """This class represents a MagicClass with methods"""

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Parameters:
        - radius (int or float): The radius of the circle. Default is 0.

        Raises:
        - TypeError: If radius is not a number.
        """
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of the circle."""
        return (2 * math.pi * self.__radius)
