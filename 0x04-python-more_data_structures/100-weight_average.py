#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_sc = sum(score * weight for score, weight in my_list)
    total_wght = sum(weight for _, weight in my_list)

    if total_wght == 0:
        return 0

    return total_sc / total_wght
