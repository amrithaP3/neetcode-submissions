# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        # will be utilizing the sametree question's logic
        # TIME COMPLEXITY: O(tree1 * tree2)

        # note: null subtree is a subtree of a null tree
        
        if not root and not subroot:
            return True
        elif not root:
            return False
        elif not subroot:
            return True

        if self.isSame(root, subroot):
            return True
        
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)
        

    def isSame(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True

        if root and subroot and root.val == subroot.val:
            return self.isSame(root.left, subroot.left) and self.isSame(root.right, subroot.right)
        else:
            return False