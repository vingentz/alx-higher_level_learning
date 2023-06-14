#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nlist = my_list[:]
    for k in range(len(nlist)):
        if nlist[k] == search:
            nlist[k] = replace
            return nlist
