#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Node is where data stored in the linked list
# each node also holds a pointer, which is a reference to the next node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


"""
Linked List
- insert
- size
- search
- delete
"""

class LinkedList(object):
    # linked list doesn't necessarily require a node to initialize, head argument will default to None
    def __init__(self, head=None):
        self.head = head

    # insert
    def insert(self, data):
        new_node = Node(data)
        #  the simplest way to do it is to place it at the head of the list
        # and point the new node at the old head
        new_node.set_next(self.head)
        self.head = new_node

    # size
    """
    The time complexity of size is O(n) because each time the
    method is called it will always visit every node in the list
    but only interact with them once, so n * 1 operations
    """
    def size(self):
        """
        starts at the head node, travels down the line of nodes
        until it reaches the end (the current will be None when
        it reaches the end) while keeping track of how many nodes it has seen
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    # search
    # The time complexity of search is O(n) in the worst case
    def search(self, data):
        """
         similar to size, but instead of traversing the whole list
        of nodes it checks at each stop to see whether the current
        node has the requested data and if so, returns the node holding that data
        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data is not in the list")
        return current

    # delete
    """
    similar to search
    traverses the list in the same way that search does,
    but in addition to keeping track of the current node,
    the delete method also remembers the last node it visited.

    The time complexity for delete is also O(n)
    """
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data is not in the list")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
