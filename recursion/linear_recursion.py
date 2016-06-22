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


# recursive algorithms for computing powers
def power(x, n):
    '''compute the value x ** n for integer n'''
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(4, 3))

def power_better(x, n):
    '''compute the value x ** n for integer n.'''
    if n == 0:
        return 1
    else:
        partial = power_better(x , n // 2)    # rely on truncated division
        result = partial * partial
        if n % 2 == 1:    # if n odd, include extra factor of x
            result *= x
        return result

print(power_better(4, 4))
