#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
二叉树：一个节点最多有两个孩子节点的树。
如果是从0索引开始存储，那么对应于节点p的孩子节点是2p+1和2p+2两个节点，
相反，节点p的父亲节点是(p-1)/2位置上的点
'''

# 直接使用list来实现二叉树，可读性差
'''
def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        # new_branch becomes the left node of root, and original left
        # node t becomes left node of new_branch, right node is none
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
print(r)                    # [3, [5, [4, [], []], []], [7, [], [6, [], []]]]
l = get_left_child(r)
print(l)                    # [5, [4, [], []], []]
set_root_val(l, 9)
print(r)                    # [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
insert_left(l, 11)
print(r)                    # [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
print(get_right_child(get_right_child(r)))      # [6, [], []]
'''

# ---------------------------------------------------------------------------------------------
# 使用类的形式定义二叉树，可读性更好
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

r = BinaryTree('a')
print(r.get_root_val())             # a
print(r.get_left_child())           # None
r.insert_left('b')
print(r.get_left_child())           # <__main__.BinaryTree object at 0x7fddefd2f518>
print(r.get_left_child().get_root_val())        # b
r.insert_right('c')
print(r.get_right_child())          # <__main__.BinaryTree object at 0x7fddefd2f550>
print(r.get_right_child().get_root_val())       # c
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())       # hello
