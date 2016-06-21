#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# a recursive function for reporting disk usage of a file system

import os

def disk_usage(path):
    '''return the number of bytes used by a file/folder and any descendents '''
    total = os.path.getsize(path)    # account for direct usage
    if os.path.isdir(path):    # if this is a directory
        for filename in os.listdir(path):    # then for each child:
            childpath = os.path.join(path, filename)    # compose full path to child
            total += disk_usage(childpath)    # add child's usage to total

    print('{0:<7}'.format(total), path)    # descriptive output (optinal)
    return total    # return the grand total

print(disk_usage('/home/lucky/Documents/Code/Python'))
