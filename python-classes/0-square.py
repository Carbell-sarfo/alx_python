try:
    square1 = Square(5)
    print("square1 size:", square1._Square__size)  # Accessing private attribute directly (not recommended)
    
    square2 = Square(-2)  # This will raise a ValueError
except ValueError as ve:
    print("Error:", ve)
except TypeError as te:
    print("Error:", te)