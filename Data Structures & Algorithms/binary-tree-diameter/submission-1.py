# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def calculate_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively find the depth of left and right subtrees
            left_depth = calculate_depth(node.left)
            right_depth = calculate_depth(node.right)
            
            # Update the global maximum diameter if the path through 
            # the current node is larger than what we've seen so far
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # Return the depth of the current subtree to its parent
            return 1 + max(left_depth, right_depth)
            
        calculate_depth(root)
        return self.max_diameter