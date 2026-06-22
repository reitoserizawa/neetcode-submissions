class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            cur = 1

            for dr, dc in DIRS:
                nr, nc = dr+r, dc+c
                if (0 <= nr < ROWS) and (0 <= nc < COLS):
                    cur += dfs(nr, nc)
                
            return cur

        for r in range(ROWS):
            for c in range(COLS):
                self.maxArea = max(self.maxArea, dfs(r, c))
    
        return self.maxArea