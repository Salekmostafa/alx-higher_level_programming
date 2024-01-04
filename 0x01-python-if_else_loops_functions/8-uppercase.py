#!/usr/bin/python3
def uppercase(my_str):
    """Print a string in uppercase."""
    for c in my_str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
