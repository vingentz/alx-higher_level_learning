#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        largest = my_list[0]
        for k in my_list:
            if k > largest:
                largest = k
        return largest
    else:
        return None
