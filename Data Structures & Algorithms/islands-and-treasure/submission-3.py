class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        def bfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or (r, c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r, c))
            q.append((r, c))


        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in DIRS:
                    bfs(dr+r, dc+c)
            dist += 1
            