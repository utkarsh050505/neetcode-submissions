# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        ans = []

        while q:
            level = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            ans.append(level[0])
        
        return ans