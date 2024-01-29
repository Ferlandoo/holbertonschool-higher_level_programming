#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            elements += 1
        except IndexError:
            print("Index Error")
        except ValueError:
            print("Value Error")
        except TypeError:
            print("Type Error")
    print("")
    return elements
