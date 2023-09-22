"""
This module defines Same class or inherit from.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
    obj: The object to be checked.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a_class or its subclass; otherwise, False.
    """
    return isinstance(obj, a_class)
