import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print(f"Number of argument(s): {num_arguments}{'s' if num_arguments != 1 else ''}:")
    print("." if num_arguments == 0 else "")

    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")