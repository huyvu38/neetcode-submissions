# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            #Swap
            node.left, node.right = node.right, node.left
            #Append if it not null
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root