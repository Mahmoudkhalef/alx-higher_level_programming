#!/usr/bin/python3

"""Module for saving to json"""
import os
import sys
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
list = []
if os.path.exists(file) == False:
    add = save_to_json_file(list, file)

for x in argv[1:]:
    list.append(x)

save_to_json_file(list, file)
