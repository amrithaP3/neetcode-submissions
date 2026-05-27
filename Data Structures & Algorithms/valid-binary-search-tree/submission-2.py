# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # keep updating left and right boundaries during recursion
        def dfs(curr, left, right):
            if not curr:
                return True

            if left < curr.val < right:
                return dfs(curr.left, left, curr.val) and dfs(curr.right, curr.val, right)
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))

        
            