class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        seen = defaultdict(int)
        longest = 0
        l = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            longest = max(longest, seen[s[r]])
            if (r - l + 1) - longest <= k:
                res = max(res, r - l + 1)
            else:
                seen[s[l]] -= 1
                l += 1
        return res

