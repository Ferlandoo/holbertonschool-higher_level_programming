#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = ""
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':' and i != len(text) - 1:
            new_text += text[i]
            new_text += "\n\n"
        else:
            new_text += text[i]
    print(new_text, end="")
