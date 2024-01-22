#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    max_length = len(sys.argv) - 1
    if max_length == 0:
        print("{} arguments.".format(max_length))
    elif max_length == 1:
        print("{} argument.".format(max_length))
        print("{}: {}".format(max_length, sys.argv[1]))
    else:
        print("{} arguments:".format(max_length))
        for i in range(1, max_length + 1):
            print("{}: {}".format(i, sys.argv[i]))
