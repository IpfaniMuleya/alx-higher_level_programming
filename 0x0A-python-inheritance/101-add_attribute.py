#!/usr/bin/python3
"""Defines a function add_attribute"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
        - obj: The object to which the attribute should be added.
        - attribute: The attribute name.
        - value: The value of the attribute.

    Raises:
        - TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
