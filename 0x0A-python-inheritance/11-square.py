#!/usr/bin/python3
"""
Module defining the Square class
"""

from 9-rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a new Square instance

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square

        Returns:
            str: The square description in the format [Square]
        """
        return "[Square] {}/{}".format(self.width, self.height)
