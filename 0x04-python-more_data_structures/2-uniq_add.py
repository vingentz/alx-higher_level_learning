#!/usr/bin/python3
def uniq_add(my_list=[]):
    k = 0
    for l in set(my_list):
        k += l
    return k
