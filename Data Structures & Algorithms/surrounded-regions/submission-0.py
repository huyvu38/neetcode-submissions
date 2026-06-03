class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        m, n = len(board), len(board[0])
        visited = set()

        def dfs(i, j):
            if (i < 0 or j < 0 or i >= m or j >= n or 
                board[i][j] != "O" or (i, j) in visited):
                return
            
            visited.add((i, j))
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # mark safe cells
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # flip surrounded ones
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"