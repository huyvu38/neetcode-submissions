class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # node found

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            # find successor
            successor = root.right
            while successor.left:
                successor = successor.left

            #replace root with current successor
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root