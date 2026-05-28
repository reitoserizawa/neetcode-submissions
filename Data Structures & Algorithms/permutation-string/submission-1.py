class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        l, r = 0, len(s1)-1

        while r < len(s2):
            if Counter(s2[l:r+1]) == cnt:
                return True
            l += 1
            r += 1
        
        return False