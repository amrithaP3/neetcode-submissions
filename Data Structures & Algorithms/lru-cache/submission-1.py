class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.nex = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.nex = self.right
        self.right.prev = self.left

    # helper functions for LL

    def remove(self, node):
        node.prev.nex = node.nex
        node.nex.prev = node.prev

    # inserting at the right (most recently used)
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
            
            # removing and reinserting node at the end of the list
            # since most recently used at this point
            self.remove(node)
            self.insert(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.nex
            self.remove(lru)
            del self.cache[lru.key]




