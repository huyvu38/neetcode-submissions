# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if subRoot is None:
            return True
        if subRoot is not None and root is None:
            return False
        def isSame(root, subRoot):
            #Both notNone
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            return root.val == subRoot.val and isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or isSame(root,subRoot)
        