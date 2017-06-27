#!usr/bin/env python
import heapq

class DijkstraPriorityQueue(object):
    PRIORITY = 0
    KEY = 1
    INDEX = 2

    def __init__(self, keys=[]):
        self.heap = keys
        heapq.heapify(self.heap)
        self.entry_finder = {}

    def add_entry(self, key, priority=float('inf')):
        entry = [priority, key]
        self.heap.append(entry)
        pos = self.siftdown(0, len(self.heap) - 1)
        self.entry_finder[key] = [priority, pos]

    def decrease_key(self, key, new_priority):
        pos = self.entry_finder[key][self.INDEX]
        del self.heap[pos]

    def siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if self.cmp_lt(newitem, parent):
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
        return pos

    @staticmethod
    def cmp_lt(x, y):
        # Use __lt__ if available; otherwise, try __le__.
        # In Py3.x, only __lt__ will be called.
        return (x < y) if hasattr(x, '__lt__') else (not y <= x)
