class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)
        
        for l in t:
            target[l] += 1
        
        l = 0
        have, need = 0, len(target)
        seen = defaultdict(int)
        resLen = float('inf')
        res = ''

        for r in range(len(s)):
            if s[r] in target:
                seen[s[r]] += 1
                if seen[s[r]] == target[s[r]]:
                    have += 1
            while have == need:
                if resLen > (r-l)+1:
                    res = s[l:r+1]
                    resLen = (r-l)+1
                
                seen[s[l]] -= 1
                if s[l] in target and seen[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        return res
            