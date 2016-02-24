#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
A new function called base_converter, shown below, takes a
decimal number and any base between 2 and 16 as parameters
'''

from Stack import Stack
def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ''
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

print(base_converter(25, 2))            # 11001
print(base_converter(25, 16))           # 19
