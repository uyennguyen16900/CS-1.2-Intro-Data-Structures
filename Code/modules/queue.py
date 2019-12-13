from .linkedlist import *

class Queue:
    def __init__(self, items=None):
        self.list = LinkedList(items)
        self.len = 0

    def __str__(self):
        return " ".join(self)

    def __iter__(self):
        """"""
        return self.list.__iter__()

    def length(self):
        """Return the length of the queue"""
        return self.len

    def enqueue(self, item):
        """Append an item into the back of the queue"""
        self.list.append(item)
        self.len += 1

    def dequeue(self):
        """Remove the first item in the queue"""
        item = self.list.head
        if self.length() > 0:
            self.list.delete(item.data)
            self.len -= 1
            return item.data
        else:
            print("This queue is empty.")
