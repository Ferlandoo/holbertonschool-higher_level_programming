#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(0, x):
            print(my_list[idx], end="")
        print()
        return idx + 1
    except IndexError:
        print()
        return idx
