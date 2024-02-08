#!/usr/bin/python3
import sys

SaveFile = __import__('5-save_to_json_file')
LoadFile = __import__('6-load_from_json_file')

filename = "add_item.json"
my_list = []
my_list = LoadFile.load_from_json_file(filename)
for idx in range(1, len(sys.argv)):
    my_list.append(sys.argv[idx])
SaveFile.save_to_json_file(my_list, filename)