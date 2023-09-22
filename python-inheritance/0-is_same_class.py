"""
This module defines a function to check if an object is exactly an instance of the specified class.
"""

def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
