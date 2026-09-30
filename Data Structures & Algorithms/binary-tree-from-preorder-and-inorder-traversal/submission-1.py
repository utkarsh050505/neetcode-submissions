class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map values to their indices for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track the current root position in the preorder traversal
        self.pre_idx = 0
        
        def helper(in_left, in_right):
            # If there are no elements to construct the subtree
            if in_left > in_right:
                return None
            
            # Select the current root value from preorder traversal
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            self.pre_idx += 1
            
            # Split the inorder list into left and right subtrees
            root_idx = inorder_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = helper(in_left, root_idx - 1)
            root.right = helper(root_idx + 1, in_right)
            
            return root
            
        return helper(0, len(inorder) - 1)
