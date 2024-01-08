#!/usr/bin/python3
"""Defines a MyInt class that inherits from int"""


class MyInt(int):
    """
    A class representing MyInt, inheriting from int.
    """

    def __eq__(self, other):
        """Overrides the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return super().__eq__(other)
