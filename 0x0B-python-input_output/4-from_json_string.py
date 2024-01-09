#!/usr/bin/python3
"""Module for getting an object represented by a JSON string."""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
