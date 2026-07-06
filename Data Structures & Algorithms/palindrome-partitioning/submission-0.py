class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]
        
        res = []

        def dfs(start, end, cur):
            if end == len(s):
                res.append(cur.copy())
                return
                    
            for end in range(start, len(s)):
                if isPalindrome(s[start:end+1]):
                    cur.append(s[start:end+1])
                    dfs(end+1, end+1, cur)
                    cur.pop()
        
        dfs(0, 0, [])

        return res