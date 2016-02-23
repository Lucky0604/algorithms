#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
选择排序(selection sort)：每个回合都选择出剩下的元素中最大的那个，
选择的方法是首先默认第一元素是最大的，如果后面的元素比它大的话，
那就更新剩下的最大的元素值，找到剩下元素中最大的之后将它放入到合适的位置就行了。
和冒泡排序类似，只是找剩下的元素中最大的方式不同而已。时间复杂度O(n2)
'''

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]

a_list = [54, 26, 33, 21, 20]
selection_sort(a_list)
print(a_list)           # [20, 21, 26, 33, 54]


# tip
'''
>>> range(1,5) #代表从1到5(不包含5)
[1, 2, 3, 4]
>>> range(1,5,2) #代表从1到5，间隔2(不包含5)
[1, 3]
>>> range(5) #代表从0到5(不包含5)
[0, 1, 2, 3, 4]
'''
