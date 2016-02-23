#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 队列：FIFO结构，先进先出
# Completed implementation of a queue ADT

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('hello')
q.enqueue('world')
print(q.items)          # ['world', 'hello']
q.enqueue(3)
q.dequeue()
print(q.items)          # ['world', 'hello']
