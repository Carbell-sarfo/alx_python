"""
This module defines a function to check if an object is an instance of a class that inherited (directly or indirectly)
from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if the given object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
