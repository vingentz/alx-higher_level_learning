#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total = []
    totalweight = 0

    for score, weight in my_list:
        total.append(score * weight)
        totalweight += weight
    weight_average = sum(total) / totalweight
    return weight_average
