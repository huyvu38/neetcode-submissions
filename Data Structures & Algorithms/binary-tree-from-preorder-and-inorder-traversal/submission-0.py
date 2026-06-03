class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Map each value to its index
        indices = {val: idx for idx, val in enumerate(inorder)}

        # Pointer to track current root in preorder
        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            # Find root position in inorder
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)