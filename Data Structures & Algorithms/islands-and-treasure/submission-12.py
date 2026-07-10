class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr+r, dc+c
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == INF:
                            grid[nr][nc] = grid[r][c] + 1
                            q.append((nr, nc))