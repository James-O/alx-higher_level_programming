#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1 or my_list is None:
        return None
    maxz = my_list[0]
    for i in my_list:
        if i > maxz:
            maxz = i
    return maxz
