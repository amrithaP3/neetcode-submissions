# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # algorithm for level order traversal = BFS
        res = []

        q = deque()
        q.append(root)

        while q:
            # iterating through q length ensures that we go through
            # one level at a time!
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()

                # handles the possible addition of null children
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            # only add level if is not empty (could have been null children)
            if level:
                res.append(level)
        
        return res






