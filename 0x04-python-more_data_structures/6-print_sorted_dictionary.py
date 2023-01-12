#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    all_keys = list(a_dictionary.keys())
    all_keys.sort()
    for i in all_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
