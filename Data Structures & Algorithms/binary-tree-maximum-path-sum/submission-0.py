# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        self.max_value = root.val
        def total(node):
            if not node:
                return 0
            cur_value = node.val
            #ignore if any below path is less than 0
            left = max(total(node.left), 0)
            right = max(total(node.right), 0)
            self.max_value = max(self.max_value, cur_value + left + right)
            #return is to handle the case when can only choose N-L or N-R
            return cur_value + max(left, right)
        total(root)
        return self.max_value