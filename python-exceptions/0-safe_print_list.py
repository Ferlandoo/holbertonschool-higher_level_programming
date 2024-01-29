#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in my_list[:x]:
            print(idx, end="")
    except IndexError:
        print()
        return idx
    print()
    return idx
