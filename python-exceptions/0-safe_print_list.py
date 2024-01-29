#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in my_list[:x]:
            print(idx, end="")
        print()
        return idx
    except IndexError:
        print()
        return idx
