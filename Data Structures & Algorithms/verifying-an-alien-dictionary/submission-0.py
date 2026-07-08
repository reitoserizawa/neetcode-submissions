class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters = {}

        for i, l in enumerate(order):
            letters[l] = i

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if letters[w1[j]] > letters[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        
        return True