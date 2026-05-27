# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        # returning HEIGHT not diameter - must use that to compute diameter!
        # diameter = left + right (WIDTH!!)
        def dfs(curr):
            # to reference variable defined outside the inner function!
            nonlocal maxDiameter

            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            #  update max diameter if path through current node is longer
            maxDiameter = max(maxDiameter, left + right)

            # return height to parent
            return 1 + max(left, right)

        dfs(root)
        return maxDiameter 

