class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited, prev_height):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r, c) in visited:
                return
            # ronly go to cells that are >= prev_height
            if heights[r][c] < prev_height:
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Pacific
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])

        # Atlantic
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        # Intersection
        return [[r, c] for (r, c) in pac & atl]
