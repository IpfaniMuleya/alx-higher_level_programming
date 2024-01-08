#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the
    specified class; otherwise False.
    """
    return type(obj) is a_class
