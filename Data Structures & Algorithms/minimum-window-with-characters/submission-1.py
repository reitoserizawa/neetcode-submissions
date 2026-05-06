class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "":
            return ""

        # count letters for s and t
        countT, window = {}, {}
        for l in t:
            countT[l] = 1 + countT.get(l, 0)

        # initialize have and need
        l = 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')

        for r in range(len(s)):
            cur = s[r]
            window[cur] = 1 + window.get(cur, 0)
            if cur in countT and window[cur] == countT[cur]:
                have += 1

            while have == need:
                # update res
                if resLen > r - l + 1:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        ss, ee = res
        return s[ss:ee+1] if resLen != float('inf') else ""