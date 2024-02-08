#!/usr/bin/python3
import sys

SaveFile = __import__('5-save_to_json_file')
LoadFile = __import__('6-load_from_json_file')

filename = "add_item.json"
my_list = []
my_list.extend(sys.argv[1:])
SaveFile.save_to_json_file(my_list, filename)
LoadFile.load_from_json_file(filename)
