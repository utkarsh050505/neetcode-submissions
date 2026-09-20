# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def dfs(self, root):
        if not root:
            return 0
        
        return max(self.dfs(root.left), self.dfs(root.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        q = deque([root])

        while q:
            node = q.popleft()
            leftDepth = 0
            rightDepth = 0
            if node.left:
                leftDepth = self.dfs(node.left) 
                q.append(node.left)
            if node.right:
                rightDepth = self.dfs(node.right)
                q.append(node.right)
            
            d = max(d, leftDepth + rightDepth)
        
        return d