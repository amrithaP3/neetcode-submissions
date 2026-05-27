class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.nex = None

class LRUCache:
    # hashmap and doubly linked list!!
    def __init__(self, capacity: int):
        self.capacity = capacity

        # hashmap/dictionary to map key to node in cache
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.nex = self.right
        self.right.prev = self.left
    
    # remove and insert = helper functions for linked list
    
    # remove node from LL from left (LRU)
    def remove(self, node):
        node.prev.nex = node.nex
        node.nex.prev = node.prev
    
    # insert node into LL at right (MRU)
    def insert(self, node):
        p = self.right.prev
        n = self.right

        p.nex = node
        node.prev = p
        node.nex = n
        n.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # updating/reordering LL (lru, mru wise)
            self.remove(node)
            self.insert(node)

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # eviction check
        if len(self.cache) > self.capacity:
            # remove from LL and delete LRU from dict
            lru = self.left.nex
            # removing from LL
            self.remove(lru)

            # deleting from hashmap/dict
            del self.cache[lru.key]

