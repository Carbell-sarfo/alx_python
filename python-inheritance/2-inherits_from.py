"""
This module defines a function for checking if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if 'obj' is an instance of a class inherited from 'a_class', False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

# Example usage:
if __name__ == "__main__":
    class BaseClass:
        pass

    class SubClass(BaseClass):
        pass

    obj1 = SubClass()
    obj2 = BaseClass()

    print(inherits_from(obj1, BaseClass))  # Should print True (SubClass inherits from BaseClass)
    print(inherits_from(obj2, SubClass))   # Should print False (BaseClass does not inherit from SubClass)