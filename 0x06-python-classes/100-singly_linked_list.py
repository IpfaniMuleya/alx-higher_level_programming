#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class."""


class Node:
    """This class represents a node of a singly linked list. """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - data: The data of the node.
        - next_node (Node): The next node in the linked list.

        Raises:
        - TypeError: If not an integer or next_node is not None or a Node.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data attribute.

        Returns:
        - int: The data of the node.

        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Setter method to set the data attribute.

        Parameters:
        - value: The data to set.

        Raises:
        - TypeError: If value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next_node attribute.

        Returns:
        - Node or None: The next node in the linked list.

        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node attribute.

        Parameters:
        - value (Node or None): The next node to set.

        Raises:
        - TypeError: If value is not None or a Node.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list."""

    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""

        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Parameters:
        - value: The value to insert.

        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Prints the entire list in stdout, one node number by line.

        Returns:
        - str: The string representation of the linked list.

        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
