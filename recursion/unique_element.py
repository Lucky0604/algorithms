#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 用递归的方法实现检测唯一元素
def unique(S, start, stop):
    '''return true if there are no duplicate elements in slice S[start: stop]'''
    if stop - start <= 1:
        return True    # at most one item
    elif not unique(S, start, stop - 1):
        return False    # first part has duplicate
    elif not unique(S, start + 1, stop):
        return False    # second part has duplicate
    else:
        return S[start] != S[stop - 1]    # do first and last differ

print(unique([1,1,4,5,33,2,66], 0, 5))    # False
print(unique([1,1,4,5,33,2,66], 1, 5))    # True
