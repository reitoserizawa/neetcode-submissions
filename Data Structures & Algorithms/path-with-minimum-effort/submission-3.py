class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(heights), len(heights[0])

        # effort map to (r, c) position
        dp = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        dp[0][0] = 0

        hp = [(0, 0, 0)]
        while hp:
            effort, r, c = heapq.heappop(hp)

            if r == ROWS-1 and c == COLS-1:
                return effort
            
            if effort > dp[r][c]:
                continue
            
            for dr, dc in DIRS:
                nr, nc = dr+r, dc+c
                if (0 <= nr < ROWS) and (0 <= nc < COLS):
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(diff, effort)

                    if new_effort < dp[nr][nc]:
                        dp[nr][nc] = new_effort
                        heapq.heappush(hp, (new_effort, nr ,nc))
