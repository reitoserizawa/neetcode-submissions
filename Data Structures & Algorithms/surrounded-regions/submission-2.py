class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        copyBoard = [['X'] * COLS for _ in range(ROWS)]
        visited = set()
        
        def dfs(r, c, visited):
            if board[r][c] != 'O':
                return
            
            visited.add((r, c))
            for dr, dc in DIRS:
                nr, nc = dr+r, dc+c
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and (nr, nc) not in visited and board[nr][nc] == 'O':
                    dfs(nr, nc, visited)

        
        for r in range(ROWS):
            dfs(r, 0, visited)
            dfs(r, COLS-1, visited)

        for c in range(COLS):
            dfs(0, c, visited)
            dfs(ROWS-1, c, visited)
        
        for r in range(ROWS):
            for c in range(COLS):
                if not (r, c) in visited:
                    board[r][c] = 'X'
        
