#!/usr/bin/python3.4
if __name__ == "__main__":
    from hidden_4 import *
    for str in dir():
        if str[:2] != "__":
            print("{}".format(str))
