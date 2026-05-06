class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longestStr = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longestStr = max(longestStr, r - l + 1)

        return longestStr