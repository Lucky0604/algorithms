#!/usr/bin/env python3
#-*- coding: utf-8 -*-



def binary_search(data, target, low, high):
    '''
    return true if target is found in indicated portion of a Python list
    the search only considers the portion from data[low] to data[high] inclusive
    '''
    if low > high:
        return False    # interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True    # found a match
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)



