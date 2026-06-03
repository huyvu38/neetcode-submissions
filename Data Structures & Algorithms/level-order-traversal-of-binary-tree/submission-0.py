# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque()
        res = []
        queue.append(root)
        while queue:
          level = []
          for _ in range(len(queue)):
            element = queue.popleft()
            level.append(element.val)
            if element.left is not None:
                queue.append(element.left)
            if element.right is not None:
                queue.append(element.right)
          res.append(level)
        return res
        