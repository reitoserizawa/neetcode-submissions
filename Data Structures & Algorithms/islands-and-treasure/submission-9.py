class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        def bfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))
        
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = level
                for dr, dc in DIRS:
                    nr, nc = dr+r, dc+c
                    bfs(nr, nc)
            level += 1

