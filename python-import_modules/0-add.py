# a = 1
# b = 2

# # Import the function from add_0.py
# from add_0 import add

# # Print the result of the addition using string formatting
# print(f"{a} + {b} = {add(a, b)}")

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    result = add(a, b)

    # print(f"{a} + {b} = {result}")
    print("{} + {} = {}".format(a, b, result))
