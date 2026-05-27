# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return (0, True)
            
            leftHeight, leftBalanced = dfs(curr.left)
            rightHeight, rightBalanced = dfs(curr.right)

            balanced = (
                leftBalanced and rightBalanced 
                and abs(leftHeight - rightHeight) <= 1
            )

            return (1 + max(leftHeight, rightHeight), balanced)
        
        return dfs(root)[1]