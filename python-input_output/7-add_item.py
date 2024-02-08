#!/usr/bin/python3
import sys

SaveFile = __import__('5-save_to_json_file').save_to_json_file
LoadFile = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []
my_list.append(sys.argv)
SaveFile.save_to_json_file(my_list, filename)
LoadFile.load_from_json_file(filename)
