#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from time import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 查看算法运行时间
start_time = time()
print(factorial(100))
end_time = time()
elapsed = end_time - start_time
print(elapsed)
