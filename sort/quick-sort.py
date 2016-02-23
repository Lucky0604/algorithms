#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
想法一：它选择第一个元素作为主元，
它同样可以按照下面提到的算法导论中将数组分成了4个不同的部分，
但是这里其实有更好的解释方法。首先，它每次都是选择第一个元素都为主元，
这个回合就是要确定主元的位置；然后，有两个指针，一个leftmark指向主元的后面一个位置，
另一个rightmark指向要排序的数组最后一个元素；接着，两个指针分别向中间移动，
leftmark遇到比主元大的元素停止，rightmark遇到比主元小的元素停止，
如果此时leftmark<rightmark，也就是说中间还有未处理(未确定与主元大小关系)的元素，
那么就交换leftmark和rightmark位置上的元素，然后重复刚才的移动操作，
直到rightmark<leftmark；最后，停止移动时候rightmark就是主元要放置的位置，
因为它停在一个比主元小的元素的位置上，之后交换主元和rightmark指向的元素即可。
完了之后，递归地对主元左右两边的数组进行排序即可。
'''

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark

a_list = [22, 1, 15, 33, 5]
quick_sort(a_list)
print(a_list)
