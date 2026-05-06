class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    count += 1
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while count > 0:
            for _ in range(len(q)):
                r, c, cur = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr+r, dc+c
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if grid[nr][nc] == -1:
                            continue
                        if grid[nr][nc] == INF:
                            grid[nr][nc] = min(cur + 1, grid[nr][nc])
                            count -= 1
                            q.append((nr, nc, cur + 1))