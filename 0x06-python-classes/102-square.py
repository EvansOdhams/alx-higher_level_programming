#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self._size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return the area of the square."""
        return self._size ** 2

    def __eq__(self, other):
        """Check if two squares are equal in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal in area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal in area, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the current square is smaller than the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the current square is smaller or equal to the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the current square is greater than the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the current square is greater or equal to the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the curruare is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
