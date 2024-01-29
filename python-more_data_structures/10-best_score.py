#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_val = max(set(a_dictionary.values()))
        key = list(filter(lambda x: a_dictionary[x] == max_val, a_dictionary))[0]
        return key
    else:
        return None
