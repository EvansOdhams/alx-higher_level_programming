#!/bin/usr/python3


class MyInt(int):
    """
    Represents a rebel integer.
    """

    def __eq__(self, other):
        """
        Checks if the value of the MyInt object is not equal to
        the other value.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Checks if the value of the MyInt object is equal to
        the other value.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if values are equal, False otherwise.
        """
        return super().__eq__(other)
