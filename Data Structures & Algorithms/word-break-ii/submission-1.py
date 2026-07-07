class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(' '.join(cur.copy()))
                return
            
            for w in wordDict:
                n = len(w)
                if i+n <= len(s) and s[i:i+n].lower() == w.lower():
                    cur.append(w)
                    dfs(i+n, cur)
                    cur.pop()
        dfs(0, [])

        return res