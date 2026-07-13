class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c)) 

            for dr, dc in DIRS:
                nr, nc = dr+r, dc+c
                if ((0 <= nr < ROWS) and (0 <= nc < COLS) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited):
                    dfs(nr, nc, visited)

        # pac
        for c in range(COLS):
            dfs(0, c, pacific)
        
        for r in range(ROWS):
            dfs(r, 0, pacific)
        
        # atl
        for c in range(COLS):
            dfs(ROWS-1, c, atlantic)

        for r in range(ROWS):
            dfs(r, COLS-1, atlantic)
        
        # res
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res
