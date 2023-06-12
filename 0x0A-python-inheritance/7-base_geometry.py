#!/usr/bin/python3
"""Define the class"""


class BaseGeometry:
    """
    BaseGeometry class representing a geometric shape.
    """

    def area(self):
        """
        Compute the area of the geometric shape.

        Raises:
            Exception: This method should be implemented in the child class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
