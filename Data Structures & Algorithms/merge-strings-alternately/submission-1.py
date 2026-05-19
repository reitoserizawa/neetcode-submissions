class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''

        l1, l2 = len(word1)-1, len(word2)-1
        i, j = 0, 0

        while i <= l1 and j <= l2:
            s += word1[i] + word2[j]
            i += 1
            j += 1
        
        if i <= l1:
            s += word1[i:]
        if j <= l2:
            s += word2[j:]
        
        return s