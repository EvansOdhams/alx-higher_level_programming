#!/usr/bin/python3
"""Define a Class"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attribute: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, "__dict__"):
        obj.__setattr__(attribute, value)
    else:
        raise TypeError("can't add new attribute")
