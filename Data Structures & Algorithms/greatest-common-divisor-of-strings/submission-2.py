class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(r):
            if len1 % r or len2 % r:
                return False
            f1, f2 = len1//r, len2//r
            return str1 == str1[:r] * f1 and str2 == str1[:r] * f2

        for r in range(min(len1, len2), 0, -1):
            if isDivisor(r):
                return str1[:r]
        
        return ''