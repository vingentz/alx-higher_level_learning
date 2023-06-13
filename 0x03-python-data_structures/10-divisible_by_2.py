#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _list = []
    for k in my_list:
        if k % 2 == 0:
            _list.append(True)
        else:
            _list.append(False)
    return _list
