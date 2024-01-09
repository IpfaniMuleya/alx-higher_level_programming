#!/usr/bin/python3
"""
Module for converting a class instance to a JSON serializable dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for
    JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description for JSON serialization.
    """
    class_dict = obj.__dict__.copy()
    for key, value in class_dict.items():
        if hasattr(value, "__dict__"):
            class_dict[key] = value.__dict__
    return class_dict
