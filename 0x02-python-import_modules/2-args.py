#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    print("{:d} {:s}{:s}".format(num,
                                 "argument" if num <= 2 and num == 1
                                 else "arguments",
                                 "." if num == 0 else ":"))
    for arg, s in enumerate(argv):
        if arg > 0:
            print("{}: {}".format(arg, s))
