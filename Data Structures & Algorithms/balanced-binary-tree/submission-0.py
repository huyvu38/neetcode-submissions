# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if node is None:
                return 0
            left = check(node.left)
            right = check(node.right)
            if left == -1:
                return -1
            if right == -1:
                return -1
            #might be first condition when a node not balance
            if abs(right - left) > 1:
                return -1
            #other case
            return 1 + max(left, right)
        return check(root) != -1