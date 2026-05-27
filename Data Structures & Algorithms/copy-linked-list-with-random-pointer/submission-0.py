"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # TWO passes
        # 1st pass: create mapping of old to new nodes
        # 2nd pass: form pointers between nodes
       
        # default for missing keys/None OG random ptr = None
        oldToCopy = collections.defaultdict(lambda: None)
       
        # 1st pass...
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        # 2nd pass...
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]
        



