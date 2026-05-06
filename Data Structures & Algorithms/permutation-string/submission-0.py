from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}

        for l in s1:
            if l in s1_map:
                s1_map[l] += 1
            else:
                s1_map[l] = 1
        
        l = 0

        for r in range(len(s1)-1, len(s2)):
            if s1_map == Counter(s2[l:r+1]):
                return True
            l += 1
            
        return False