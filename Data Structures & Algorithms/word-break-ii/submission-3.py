class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordDict = set(wordDict)

        def dfs(i):
            if i == len(s):
                return [""]
            
            if i in memo:
                return memo[i]
                
            res =[]
            for w in wordDict:
                n = len(w)
                if i+n <= len(s) and s[i:i+n].lower() == w.lower():
                    for suffix in dfs(i+n):
                        if suffix:
                            res.append(w + ' ' + suffix)
                        else:
                            res.append(w)
            memo[i] = res
            return res

        
        return dfs(0)