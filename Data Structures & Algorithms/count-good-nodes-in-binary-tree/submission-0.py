# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # just need to check if current value is greater than the max value seen so far
        # pre-order traversal!! CLR
        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                res = 1
                maxVal = node.val
            else:
                res = 0
            
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        return dfs(root, root.val)



            

            





        