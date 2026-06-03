class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[], ]
        def dfs(index, path):
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                res.append(path[:])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res