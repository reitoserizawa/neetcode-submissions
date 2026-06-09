class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # cur_r, cur_c, cur_i
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return False
            
            if word[i] != board[r][c]:
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if dfs(nr, nc, i+1):
                    return True
            board[r][c] = tmp
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False
