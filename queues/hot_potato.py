#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
Josephus problem
'''
from Queue import Queue

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
            print(sim_queue.dequeue())
        sim_queue.dequeue()


    return sim_queue.dequeue()

print(hot_potato(['lemond', 'lucky', 'cherry', 'bill', 'jack', 'lucy'], 4))
