class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        def helper(l, r):
            if l > r:
                return True
            if s[l] != s[r]:
                return False
            return helper(l+1, r-1)
            
        while l <= r:
            if s[l] != s[r]:
                if helper(l+1, r) or helper(l, r-1):
                    return True
                else:
                    return False
            l += 1
            r -= 1
        
        return True