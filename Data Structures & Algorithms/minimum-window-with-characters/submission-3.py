class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "":
            return ""
    
        # count letters for s and t
        t_hash, window = {}, {}
        for l in t:
            t_hash[l] = 1 + t_hash.get(l, 0)

        # initialize have and need
        l = 0
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(t_hash)

        for r in range(len(s)):
            cur = s[r]
            window[cur] = 1 + window.get(cur, 0)
            if cur in t_hash and t_hash[cur] == window[cur]:
                have += 1
            
            while have == need:
                if resLen > r-l+1:
                    res = [l, r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in t_hash and window[s[l]] < t_hash[s[l]]:
                    have -= 1
                l += 1

        ss, ee = res
        return s[ss:ee+1] if resLen != float('inf') else ""