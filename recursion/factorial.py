#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from time import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def bad_fibonacci(n):
    '''return the nth Fibonacci number'''
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 2) + bad_fibonacci(n - 1)
def good_fibonacci(n):
    '''return pair of Fibonacci numbers, F(n) and F(n-1)'''
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)

# 查看算法运行时间
start_time = time()
print(factorial(100))
end_time = time()
elapsed = end_time - start_time
print(elapsed)

# 使用递归实现英式度量尺
def draw_line(tick_length, tick_label=''):
    '''
    draw one line with given tick length(followed by optional label)
    '''
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    '''
    draw tick interval based upon a central tick length
    '''
    if center_length > 0:    # stop when length drops to 0
        draw_interval(center_length - 1)    # recursively draw top ticks
        draw_line(center_length)    # recursively draw top ticks
        draw_interval(center_length - 1)    # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    '''
    draw english ruler with given number of inches, major tick length
    '''
    draw_line(major_length, '0')    # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)    # draw interior ticks for inch
        draw_line(major_length, str(j))    # draw inch j line and label
draw_interval(4)
