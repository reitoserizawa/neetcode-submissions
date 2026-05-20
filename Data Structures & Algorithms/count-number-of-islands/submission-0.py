class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        cnt = 0

        def helper(r, c):
            if (r, c) in visited:
                return
                
            visited.add((r, c))
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                    helper(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if not (r, c) in visited and grid[r][c] == "1":
                    helper(r, c)
                    cnt += 1
        
        return cnt