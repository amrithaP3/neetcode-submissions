# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Pre-order traversal (Current, Left, Right = CLR)
        # Time complexity = O(n)
        ## n = number of nodes in binary tree
        ## time complexity is determined by height of tree
        
        # Base case for recursion: node DNE 
        # handles the case when tree FULLY traversed where empty node come across
        if not root:
            return None

        # Swapping left and right nodes
        temp = root.right
        root.right = root.left
        root.left = temp

        # Traversing dwon the left subtrees
        self.invertTree(root.left)

        # Traversing down the right subtrees
        self.invertTree(root.right)
        
        return root

