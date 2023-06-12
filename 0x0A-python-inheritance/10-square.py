#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a square instance
        Args:
            size (int): The size of the square's sides
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
