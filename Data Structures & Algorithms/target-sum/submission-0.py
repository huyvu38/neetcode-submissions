class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [{} for _ in range(n + 1)]
        # base case: 1 way to get sum 0 with 0 numbers
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                # Add nums[i]
                dp[i + 1][total + nums[i]] = dp[i + 1].get(total + nums[i], 0) + count
                # Subtract nums[i]
                dp[i + 1][total - nums[i]] = dp[i + 1].get(total - nums[i], 0) + count
        print(dp)
        return dp[n].get(target, 0)