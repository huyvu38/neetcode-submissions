# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def check(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is not None and node2 is None:
                return False
            if node1 is None and node2 is not None:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)
        return check(p,q)