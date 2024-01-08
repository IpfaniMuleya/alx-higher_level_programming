#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """A class that inherits from list with additional methods."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        print(sorted(self))
