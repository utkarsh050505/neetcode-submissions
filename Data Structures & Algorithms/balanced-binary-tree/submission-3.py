# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calculate_depth(self, root):
        if root is None:
            return 0
            
        left = self.calculate_depth(root.left)
        right = self.calculate_depth(root.right)

        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.calculate_depth(root) != -1