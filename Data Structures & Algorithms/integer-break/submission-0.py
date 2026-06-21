class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for num in range(2, n+1):
            #Force to split
            if num == n:
                dp[num] = 0
            else:
                #Do not have to split if it greater than product of split numbers
                dp[num] = num
            for j in range(1, num):
              dp[num] = max(dp[num], dp[j] * dp[num-j])
        return dp[n]