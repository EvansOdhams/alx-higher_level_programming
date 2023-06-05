#!/usr/bin/python3
"""Define classes for singly lists"""


class Node:
    """Represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize a new singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value of the new Node to insert.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        if value < current.data:
            new_node.next_node = current
            self.head = new_node
            return

        while (current.next_node is not None and
               value >= current.next_node.data):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next_node

        return "\n".join(values)
