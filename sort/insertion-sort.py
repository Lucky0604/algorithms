#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
插入排序(insertion sort)：每次假设前面的元素都是已经排好序了的，
然后将当前位置的元素插入到原来的序列中，
为了尽快地查找合适的插入位置，
可以使用二分查找。时间复杂度O(n2)O(n2)，
别误以为二分查找可以降低它的复杂度，因为插入排序还需要移动元素的操作
'''

def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

def insertion_sort_binarysearch(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low = 0
        high = len(a_list) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if a_list[mid] > current_value:
                high = mid - 1
            else:
                low = mid + 1
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

a_list = [22, 13, 5, 15, 8]
insertion_sort(a_list)
print(a_list)
insertion_sort_binarysearch(a_list)
print(a_list)
