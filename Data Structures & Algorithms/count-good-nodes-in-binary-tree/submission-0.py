# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root: TreeNode, curr_max: int):
            nonlocal ans
            if root is None:
                return None
            
            if root.val >= curr_max:
                curr_max = root.val
                ans += 1
            
            left = dfs(root.left, curr_max)
            right = dfs(root.right, curr_max)
        
        dfs(root, root.val)
        return ans