class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}

        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1
        
        for char in t:
            if char in s_count:
                s_count[char] -= 1

                if s_count[char] == 0:
                    del s_count[char]
            else:
                return False
        
        return True if len(s_count) == 0 else False