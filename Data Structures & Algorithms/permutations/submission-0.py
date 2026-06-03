class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, pick):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(0, len(nums)):
                if not pick[i]:
                  pick[i] = True
                  path.append(nums[i])
                  dfs(path, pick)
                  path.pop()
                  pick[i] = False

        dfs([], [False] * len(nums))
        return res