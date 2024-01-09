#!/usr/bin/python3
"""Module for defining a Student class."""


class Student:
    """Student class definition."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
             attrs (list): A list of attribute names to retrieve.
             If None, retrieve all attributes.

        Returns:
            dict: The dictionary representation of the Student instance.

        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__
