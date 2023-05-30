#!/usr/bin/python3
"""Define the class as a Square""""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize a square object.

        Args:
            size (float or int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size ** 2

    def __eq__(self, other):
        """Compare if two squares have equal areas."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Compare if two squares have different areas."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compare if the area of self is less than the area of square."""
        if isinstance(other, Square):
            return self.area() < other.area()
        raise TypeError("unsupported operand type(s) for <")

    def __le__(self, other):
        """Compare if the area of self is less than of other square."""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Compare if the area of self is greater than square."""
        if isinstance(other, Square):
            return self.area() > other.area()
        raise TypeError("unsupported operand type(s) for >")

    def __ge__(self, other):
        """Compare if the area of self is greater than square."""
        return self.__gt__(other) or self.__eq__(other)
