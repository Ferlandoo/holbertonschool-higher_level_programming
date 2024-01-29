#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if element == search else element for element in my_list]
    return new_list



# Write a function that replaces all occurrences of an element by another in a new list.

# Prototype: def search_replace(my_list, search, replace):
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element
# You are not allowed to import any module
# guillaume@ubuntu:~/$ ./1-main.py
# [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
# [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
