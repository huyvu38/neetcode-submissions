class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            notFind = True
            for _ in range (len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                if notFind:
                  result.append(node.val)
                  notFind = False
        return result