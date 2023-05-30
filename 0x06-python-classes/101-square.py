#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Print the square with '#' characters."""
        if self._size == 0:
            print()
            return

        for _ in range(self._position[1]):
            print()
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        """Return a string representation of the square."""
        if self._size == 0:
            return ""
        
        square_str = ""
        for _ in range(self._position[1]):
            square_str += "\n"
        for _ in range(self._size):
            square_str += " " * self._position[0] + "#" * self._size + "\n"
        return square_str.rstrip()
