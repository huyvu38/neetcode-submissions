from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # iterate backwards to avoid reuse of same element
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        
        return dp[target]