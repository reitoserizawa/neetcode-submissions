class Node:
    def __init__(self):
        self.children = {}
        self.word = None
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
            cur.word = w
            cur.isEnd = True
        
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = []

        def dfs(r, c, parent):
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return
            
            ch = board[r][c]
            if ch == '#' or ch not in parent.children:
                return
            
            cur = parent.children[ch]
            board[r][c] = '#'

            if cur.isEnd:
                res.append(cur.word)
                cur.isEnd = False
            
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, cur)
            
            board[r][c] = ch

            if not cur.children and not cur.isEnd:
                del parent.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        
        return res


        