'''
同样是执行1000次创建一个包含1-1000的列表，
四种方式使用的时间差距很大！
使用append比逐次增加要快很多，另外，使用python的列表产生式比append要快，而第四种方式更加快
'''

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

# Import the timeit module -> import timeit
# Import the Timer class defined in the module
from timeit import Timer
# if the above line is excluded, you need replace Timer with timeit.Timer when defining a Timer Object
t1 = Timer('test1()', 'from __main__ import test1')
print('concat ', t1.timeit(number = 1000), 'millionseconds')
t2 = Timer('test2()', 'from __main__ import test2')
print('append ', t2.timeit(number = 1000), 'millionseconds')
t3 = Timer('test3()', 'from __main__ import test3')
print('comprehension ', t3.timeit(number = 1000), 'millionseconds')
t4 = Timer('test4()', 'from __main__ import test4')
print('list range ', t4.timeit(number = 1000), 'millionseconds')

# concat  1.2605092770027113 millionseconds
# append  0.0598407049983507 millionseconds
# comprehension  0.0291672439998365 millionseconds
# list range  0.011241537002206314 millionseconds
