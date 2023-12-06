#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_ = max(a_dictionary.values())
        best = [key for key, value in a_dictionary.items() if value == max_][0]
        return best
    else:
        return None
