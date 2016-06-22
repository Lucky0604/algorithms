#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# a recursive algorithms for computing the sum of a sequence of numbers
def linear_sum(S, n):
    ''' return the sum of the first n numbers of sequence S.'''
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]

print(linear_sum([2,3,4,5], 4))    # 14


# reversing a sequence with recursion, using linear recursion
# so as reverse(S, 0, len(S))
def reverse(S, start, stop):
    '''reverse elements in implicit slice S[start:stop]'''
    if start < stop - 1:    # if at least 2 elements
        S[start], S[stop - 1] = S[stop - 1], S[start]     # swap first and last
        reverse(S, start + 1, stop - 1)    # recur on rest

S = [2,3,5,1]
reverse(S, 0, 3)
print(S)    # [5, 3, 2, 1]
