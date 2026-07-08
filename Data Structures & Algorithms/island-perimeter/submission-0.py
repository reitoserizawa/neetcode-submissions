class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return 1

            if grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0
            
            perimeter = 0
            visited.add((r, c))

            for dr, dc in DIRS:
                perimeter += dfs(dr+r, dc+c, visited)
            
            return perimeter
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c, set())
        