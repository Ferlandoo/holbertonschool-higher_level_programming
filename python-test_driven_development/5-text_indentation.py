#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    begin = 0
    for i, j in enumerate(text):
        if j in '.?:':
            print(text[begin: i + 1].strip() + '\n')
            begin = i + 1
    if begin < len(text):
        print(text[begin:].strip(), end="")
