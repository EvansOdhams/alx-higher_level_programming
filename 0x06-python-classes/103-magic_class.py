#!/usr/bin/python3
"""Define a MagicClass"""


import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0  # Initialize the private attribute __radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")  # Check if the
        self.__radius = radius  # Set the value of __radius

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi  # Calculate and return

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius  # Calculate and return
