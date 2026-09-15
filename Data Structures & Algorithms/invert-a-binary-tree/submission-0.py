# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base Case: If the node is empty, return None
        if not root:
            return None
        
        # 2. Recursively invert the subtrees and swap them
        root.left, root.right = self.invertTree(root.right),         self.invertTree(root.left)
        
        # 3. Return the inverted tree root
        return root