#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file
"""
import sys


from os.path import exists
from json import load, dump

filename = "add_item.json"

if not exists(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        dump([], file)

with open(filename, 'r', encoding='utf-8') as file:
    my_list = load(file)

my_list.extend(sys.argv[1:])

with open(filename, 'w', encoding='utf-8') as file:
    dump(my_list, file)
