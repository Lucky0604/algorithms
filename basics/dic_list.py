#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer('random.randrange(%d) in x' % i, 'from __main__ import random, x')
    x = list(range(i))
    lst_time = t.timeit(number = 1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number = 1000)
    print('%d, %10.3f, %10.3f' % (i, lst_time, d_time))


'''
10000,      0.079,      0.001
30000,      0.164,      0.001
50000,      0.248,      0.001
70000,      0.361,      0.001
90000,      0.441,      0.001
110000,      0.554,      0.001
130000,      0.679,      0.001
150000,      0.773,      0.001
170000,      0.865,      0.001
190000,      0.970,      0.001
210000,      1.074,      0.001
230000,      1.207,      0.001
250000,      1.248,      0.001
270000,      1.421,      0.001
290000,      1.501,      0.001
310000,      1.560,      0.001
'''
# dictionary is O(1)
