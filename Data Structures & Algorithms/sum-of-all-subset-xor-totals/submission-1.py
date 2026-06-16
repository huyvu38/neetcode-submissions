class Solution(object):
    def subsetXORSum(self, nums):
        self.total = 0

        def dfs(index, cur_xor):
            self.total += cur_xor

            for i in range(index, len(nums)):
                dfs(i + 1, cur_xor ^ nums[i])

        dfs(0, 0)
        return self.total