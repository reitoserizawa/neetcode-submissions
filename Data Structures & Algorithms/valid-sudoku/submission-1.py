class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                cur = board[r][c]
                if cur == '.':
                    continue
                if cur in rows[r] or cur in cols[c] or cur in square[(r//3, c//3)]:
                    return False
                rows[r].add(cur)
                cols[c].add(cur)
                square[(r//3, c//3)].add(cur)
        return True