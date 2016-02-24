#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Converting Decimal Numbers to Binary Numbers
'''
an algorithm called “Divide by 2” that uses a stack
to keep track of the digits for the binary result.
easily convert integer values into binary numbers.
'''

from Stack import Stack

def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_string = ''
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string

print(divide_by_2(42))
