class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            if (r, c) in visited:
                return 0
            
            area = 1
            visited.add((r, c))
            for dr, dc in DIRS:
                area += dfs(dr+r, dc+c, visited)
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                self.maxArea = max(dfs(r, c, set()), self.maxArea)
        
        return self.maxArea