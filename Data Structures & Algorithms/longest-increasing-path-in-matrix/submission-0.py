class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_row = len(matrix)
        max_col = len(matrix[0])
        memo = [[0] * max_col for _ in range(max_row)]
        count = 0
        
        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]
            
            max_len = 1  # start with 1
            
            if r >= 1 and matrix[r][c] < matrix[r-1][c]:
                max_len = max(max_len, 1 + dfs(r-1, c))
                
            if c >= 1 and matrix[r][c] < matrix[r][c-1]:
                max_len = max(max_len, 1 + dfs(r, c-1))
                
            if r < max_row - 1 and matrix[r][c] < matrix[r+1][c]:
                max_len = max(max_len, 1 + dfs(r+1, c))
                
            if c < max_col - 1 and matrix[r][c] < matrix[r][c+1]:
                max_len = max(max_len, 1 + dfs(r, c+1))
            
            memo[r][c] = max_len
            return max_len
        
        for i in range(max_row):
            for j in range(max_col):
                count = max(count, dfs(i, j))
        
        return count