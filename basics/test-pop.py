#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import Timer
# 测试pop操作
x = list(range(2000000))
pop_zero = Timer('x.pop(0)', 'from __main__ import x')
print('pop_zero ', pop_zero.timeit(number = 1000), 'millionseconds')
x = list(range(2000000))
pop_end = Timer('x.pop()', 'from __main__ import x')
print('pop_end ', pop_end.timeit(number = 1000), 'millionseconds')

# pop_zero  1.5076678299956257 millionseconds
# pop_end  7.485700189135969e-05 millionseconds

# 从结果可以看出，pop最后一个元素的效率远远高于pop第一个元素
