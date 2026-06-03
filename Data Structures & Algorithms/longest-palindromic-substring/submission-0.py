class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        best = 1
        start = 0

        # length 1
        for i in range(n):
            dp[i][i] = True

        # length 2 to n
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > best:
                            best = length
                            start = i

        return s[start:start + best]
