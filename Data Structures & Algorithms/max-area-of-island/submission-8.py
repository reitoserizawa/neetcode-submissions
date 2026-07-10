class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            if grid[r][c] == '#':
                return 0
            
            area = 1
            grid[r][c] = '#'
            for dr, dc in DIRS:
                area += dfs(dr+r, dc+c)
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                self.maxArea = max(dfs(r, c), self.maxArea)
        
        return self.maxArea