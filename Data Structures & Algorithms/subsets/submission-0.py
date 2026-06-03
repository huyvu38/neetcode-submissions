class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(index, path):
            #Append a copy
            res.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res