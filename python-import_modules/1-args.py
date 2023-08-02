import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print(f"1 argument:" if num_arguments == 1 else f"{num_arguments} arguments:")

    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")