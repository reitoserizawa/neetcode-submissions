class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        for w in words:
            cur = root
            for l in w:
                if l not in cur.children:
                    cur.children[l] = Node()
                cur = cur.children[l]
            cur.isEnd = True
        
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = []

        def dfs(r, c, cur, w):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            
            if board[r][c] not in cur.children:
                return
            
            if board[r][c] == '#':
                return
            


            w.append(board[r][c])
            cur = cur.children[board[r][c]]

            tmp = board[r][c]
            board[r][c] = '#'

            if cur.isEnd:
                res.append(''.join(w))
                cur.isEnd = False
            
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, cur, w)
            
            w.pop()
            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, [])
        
        return res


        