# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        def dfs(node, current_max):
            if not node:
                return 
            if node.val >= current_max:
                count[0] +=1
                current_max=node.val
            dfs(node.left, current_max)
            dfs(node.right, current_max)
        dfs(root, root.val)
        return count[0]
    
        