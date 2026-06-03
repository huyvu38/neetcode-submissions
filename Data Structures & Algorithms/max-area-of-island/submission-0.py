class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        area = 0
        #only call bfs if find 1
        def bfs(r, c):
            q=deque()
            grid[r][c] = 0
            q.append((r,c))
            res=1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r < 0 or new_c < 0 or new_r >= len(grid) or
                        new_c >= len(grid[0]) or grid[new_r][new_c] == 0):
                        continue
                    #if it 1 then append
                    res+=1
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = 0
            return res
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                   area = max(area, bfs(i, j))
        return area

    